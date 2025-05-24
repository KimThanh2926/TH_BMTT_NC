from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# === VIGENERE CIPHER ===
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key', 'KIMTHANH')  # fallback nếu không có key
    cipher = VigenereCipher(key)
    encrypted_text = cipher.vigenere_encrypt(plain_text)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key', 'KIMTHANH')
    cipher = VigenereCipher(key)
    decrypted_text = cipher.vigenere_decrypt(cipher_text)
    return jsonify({"decrypted_text": decrypted_text})

# === CAESAR CIPHER ===
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2926, debug=True)
