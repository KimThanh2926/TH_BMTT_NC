from string import ascii_uppercase

class CaesarCipher:
    def __init__(self):
        self.alphabet = list(ascii_uppercase)

    def encrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter not in self.alphabet:
                encrypted_text.append(letter)  # giữ nguyên các ký tự đặc biệt
                continue
            index = self.alphabet.index(letter)
            output_index = (index + key) % len(self.alphabet)
            encrypted_text.append(self.alphabet[output_index])
        return "".join(encrypted_text)  # ❌ KHÔNG dùng " ".join()

    def decrypt_text(self, text: str, key: int) -> str:
        text = text.upper().replace(" ", "")  # ❗ loại bỏ khoảng trắng nếu có
        decrypted_text = []
        for letter in text:
            if letter not in self.alphabet:
                decrypted_text.append(letter)
                continue
            index = self.alphabet.index(letter)
            output_index = (index - key) % len(self.alphabet)
            decrypted_text.append(self.alphabet[output_index])
        return "".join(decrypted_text)
