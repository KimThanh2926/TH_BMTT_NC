class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def vigenere_encrypt(self, plain_text):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text