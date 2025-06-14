import cv2
import numpy as np
import sys

def encode_message_in_video(input_path, output_path, secret_message):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"❌ Không mở được video: {input_path}")
        return

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Sử dụng MJPG cho .avi
    out    = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    secret_message += "####"  # đánh dấu kết thúc
    binary_msg = ''.join(format(ord(c), '08b') for c in secret_message)
    msg_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        for i in range(height):
            for j in range(width):
                for k in range(3):  # BGR
                    if msg_idx < len(binary_msg):
                        frame[i, j, k] = (frame[i, j, k] & 0b11111110) | int(binary_msg[msg_idx])
                        msg_idx += 1
        out.write(frame)

    cap.release()
    out.release()
    print(f"✅ Đã giấu tin vào video: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("🔸 Cách dùng: python encode_video.py <input_video> <message>")
    else:
        encode_message_in_video(sys.argv[1], "encoded.avi", sys.argv[2])
