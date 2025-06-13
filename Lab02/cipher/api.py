from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

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

# === RAILFENCE CIPHER ===
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# === PLAYFAIR CIPHER ALGORITHM ===
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# === TRANSPOSITION CIPHER ALGORITHM ===
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2926, debug=True)
