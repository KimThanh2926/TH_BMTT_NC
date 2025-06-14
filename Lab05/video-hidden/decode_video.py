import cv2

def decode_message_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Không mở được video.")
        return

    binary_data = ""
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        height, width, _ = frame.shape
        for i in range(height):
            for j in range(width):
                for k in range(3):
                    binary_data += str(frame[i, j, k] & 1)

    bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ""
    for byte in bytes_data:
        try:
            decoded += chr(int(byte, 2))
            if decoded.endswith("####"):
                break
        except:
            break

    cap.release()
    if decoded.endswith("####"):
        print("🔍 Tin giấu được giải mã:")
        print(decoded[:-4])
    else:
        print("⚠️ Không tìm thấy kết thúc '####'.")
        print("🔎 Đã giải được:", decoded[:50], "..." if len(decoded) > 50 else "")

decode_message_from_video("encoded.avi")
