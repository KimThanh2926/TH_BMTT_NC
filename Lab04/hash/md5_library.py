import hashlib

def md5_hash(input_string):
    result = hashlib.md5(input_string.encode('utf-8'))
    return result.hexdigest()

if __name__ == '__main__':
    input_text = input("Nhập chuỗi: ")
    print("MD5:", md5_hash(input_text))
