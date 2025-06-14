import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            for color_channel in range(3): # Iterate through R, G, B channels
                binary_message += format(pixel[color_channel], '08b')[-1] # Get the LSB

    message = ""
    # The original encoding used '1111111111111110' as an end marker.
    # We need to look for that sequence to stop decoding.
    end_marker = '1111111111111110' 
    marker_len = len(end_marker)

    i = 0
    while i + 8 <= len(binary_message):
        byte = binary_message[i:i+8]
        # Check if the current 16 bits (two bytes) match the end marker
        if i + marker_len <= len(binary_message) and binary_message[i:i+marker_len] == end_marker:
            break
        
        char = chr(int(byte, 2))
        message += char
        i += 8

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()