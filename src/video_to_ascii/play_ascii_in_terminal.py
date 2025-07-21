import os
import time
import sys

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[35m",  # Purple
    "\033[37m",  # White
    "\033[34m",  # Blue
]
RESET = "\033[0m"

ASCII_FRAMES_DIR = os.path.join(os.path.dirname(__file__), "../../ascii_frames")
FRAME_DELAY = 0.05  # seconds between frames
COLOR_CYCLE_FRAMES = 10  # Change color every N frames


def get_ascii_frame_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    files.sort()
    return [os.path.join(directory, f) for f in files]


def print_ascii_frames():
    frame_files = get_ascii_frame_files(ASCII_FRAMES_DIR)
    color_index = 0
    frame_counter = 0
    # Hide cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    try:
        while True:
            for frame_file in frame_files:
                with open(frame_file, "r") as f:
                    ascii_art = f.read()
                color = COLORS[color_index]
                sys.stdout.write(
                    "\033[2J\033[H"
                )  # Clear entire terminal and move cursor to top left
                sys.stdout.write(f"{color}{ascii_art}{RESET}")
                sys.stdout.flush()
                time.sleep(FRAME_DELAY)
                frame_counter += 1
                if frame_counter % COLOR_CYCLE_FRAMES == 0:
                    color_index = (color_index + 1) % len(COLORS)
    finally:
        # Show cursor again
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


if __name__ == "__main__":
    try:
        print_ascii_frames()
    except KeyboardInterrupt:
        print("\nExiting...")
