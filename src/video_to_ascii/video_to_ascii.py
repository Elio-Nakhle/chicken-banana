import cv2
from PIL import Image
import os

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def frame_to_ascii(image, new_width=100):
    image = Image.fromarray(image)
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    image = image.resize((new_width, new_height))
    image = image.convert("L")
    pixels = image.getdata()
    ascii_str = ""
    for i, pixel in enumerate(pixels):
        ascii_str += ASCII_CHARS[pixel // 25]
        if (i + 1) % new_width == 0:
            ascii_str += "\n"
    return ascii_str


def video_to_ascii_txt(video_path, output_dir, width=100):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ascii_art = frame_to_ascii(gray, new_width=width)
        with open(os.path.join(output_dir, f"frame_{frame_count:05d}.txt"), "w") as f:
            f.write(ascii_art)
        frame_count += 1
    cap.release()
    print(f"Done! {frame_count} frames processed.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert video frames to ASCII art .txt files."
    )
    parser.add_argument("video_path", help="Path to the input video file")
    parser.add_argument(
        "--output_dir",
        default="ascii_frames",
        help="Directory to save ASCII art frames",
    )
    parser.add_argument("--width", type=int, default=100, help="Width of ASCII art")
    args = parser.parse_args()
    video_to_ascii_txt(args.video_path, args.output_dir, args.width)
