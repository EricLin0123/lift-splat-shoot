import os
import cv2
import argparse


def extract_frames(video_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    idx = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out_path = os.path.join(out_dir, f"{idx}.png")
        cv2.imwrite(out_path, frame)
        idx += 1
    cap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract frames from two videos into custom-data structure.")
    parser.add_argument('--front_video', type=str, required=True,
                        help='Path to front video (e.g., front.mp4)')
    parser.add_argument('--back_video', type=str, required=True,
                        help='Path to back video (e.g., back.mp4)')
    parser.add_argument('--out_root', type=str,
                        default="custom-data", help='Output root directory')
    args = parser.parse_args()

    extract_frames(args.front_video, os.path.join(args.out_root, "front"))
    extract_frames(args.back_video, os.path.join(args.out_root, "back"))
