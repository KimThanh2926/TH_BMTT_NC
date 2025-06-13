import struct
import math

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md5(message):
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

    s = [7, 12, 17, 22] * 4 + \
        [5, 9, 14, 20] * 4 + \
        [4, 11, 16, 23] * 4 + \
        [6, 10, 15, 21] * 4

    K = [int((1 << 32) * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

    message = bytearray(message)
    orig_len_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += struct.pack('<Q', orig_len_bits)

    for offset in range(0, len(message), 64):
        a, b, c, d = a0, b0, c0, d0
        chunk = message[offset:offset+64]
        M = list(struct.unpack('<16I', chunk))

        for i in range(64):
            if 0 <= i <= 15:
                F = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                F = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                F = c ^ (b | ~d)
                g = (7 * i) % 16

            F = (F + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(F, s[i])) & 0xFFFFFFFF

        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    return ''.join(['{:02x}'.format(i) for i in struct.pack('<4I', a0, b0, c0, d0)])

if __name__ == '__main__':
    input_string = input("Nhập chuỗi cần băm: ")
    md5_hash_value = md5(input_string.encode('utf-8'))
    print("Mã băm MD5 của '{}' là: {}".format(input_string, md5_hash_value))
