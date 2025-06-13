from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản: ")
    encoded_text = text.encode('utf-8')
    hashed_text = sha3(encoded_text)

    print("Chuỗi văn bản đã nhập:", text)
    print("SHA-3 (256-bit) Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()
