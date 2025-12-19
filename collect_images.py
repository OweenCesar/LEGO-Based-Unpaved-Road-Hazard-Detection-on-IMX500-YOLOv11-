#!/usr/bin/env python3
import argparse
import os
import time
from datetime import datetime

import cv2
from picamera2 import Picamera2


def parse_args():
    p = argparse.ArgumentParser(description="Collect images for a fixed duration using Picamera2.")
    p.add_argument("--out", type=str, default="captured_images", help="Output directory")
    p.add_argument("--prefix", type=str, default="img", help="Filename prefix")
    p.add_argument("--duration", type=float, default=20.0, help="Capture duration in seconds")
    p.add_argument("--interval", type=float, default=0.5, help="Seconds between saves")
    p.add_argument("--warmup", type=float, default=1.5, help="Seconds to wait before starting saves")
    p.add_argument("--width", type=int, default=1280, help="Capture width")
    p.add_argument("--height", type=int, default=720, help="Capture height")
    p.add_argument("--jpeg-quality", type=int, default=95, help="JPEG quality (0-100)")
    return p.parse_args()


def main():
    args = parse_args()
    os.makedirs(args.out, exist_ok=True)

    window_name = "PiCam Duration Collector (press 'q' to quit early)"
    saved = 0

    picam2 = Picamera2()
    config = picam2.create_preview_configuration(
        main={"size": (args.width, args.height), "format": "RGB888"}
    )
    picam2.configure(config)
    picam2.start()

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    print(f"Warmup for {args.warmup:.1f}s...")
    time.sleep(args.warmup)

    start_t = time.time()
    end_t = start_t + args.duration
    next_save_t = time.time()  # save immediately after warmup

    try:
        while True:
            frame = picam2.capture_array()
            now = time.time()

            # Save frames until duration ends
            if now >= next_save_t and now <= end_t:
                ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filename = f"{args.prefix}_{saved:06d}_{ts}.jpg"
                path = os.path.join(args.out, filename)
                ok = cv2.imwrite(path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), args.jpeg_quality])
                if ok:
                    saved += 1
                    print(f"Saved: {path}")
                else:
                    print(f"Failed to save: {path}")
                next_save_t = now + args.interval

            # HUD
            remaining = max(0.0, end_t - now)
            hud = frame.copy()
            cv2.putText(
                hud,
                f"Saved: {saved} | remaining: {remaining:4.1f}s | interval={args.interval}s | 'q' to quit",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )
            cv2.imshow(window_name, hud)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                print("Stopped early by user.")
                break

            if now > end_t:
                print(f"Done. Captured for {args.duration}s, saved {saved} images.")
                break

    finally:
        cv2.destroyAllWindows()
        picam2.stop()


if __name__ == "__main__":
    main()

