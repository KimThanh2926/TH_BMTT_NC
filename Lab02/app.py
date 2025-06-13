from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

# router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()

    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()

    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Vigenère
@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    result = None
    if request.method == "POST":
        key = request.form["key"]
        cipher = VigenereCipher(key)
        if "plain_text" in request.form:
            result = cipher.vigenere_encrypt(request.form["plain_text"])
        else:
            result = cipher.vigenere_decrypt(request.form["cipher_text"])
    return render_template("vigenere.html", result=result)

# Rail Fence
@app.route("/railfence", methods=["GET", "POST"])
def railfence():
    result = None
    if request.method == "POST":
        key = int(request.form["key"])
        cipher = RailFenceCipher()
        if "plain_text" in request.form:
            result = cipher.rail_fence_encrypt(request.form["plain_text"], key)
        else:
            result = cipher.rail_fence_decrypt(request.form["cipher_text"], key)
    return render_template("railfence.html", result=result)

# Playfair
@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    result = None
    if request.method == "POST":
        key = request.form["key"]
        cipher = PlayFairCipher()
        matrix = cipher.create_playfair_matrix(key)
        if "plain_text" in request.form:
            result = cipher.playfair_encrypt(request.form["plain_text"], matrix)
        else:
            result = cipher.playfair_decrypt(request.form["cipher_text"], matrix)
    return render_template("playfair.html", result=result)

# Transposition
@app.route("/transposition", methods=["GET", "POST"])
def transposition():
    result = None
    if request.method == "POST":
        key = int(request.form["key"])
        cipher = TranspositionCipher()
        if "plain_text" in request.form:
            result = cipher.encrypt(request.form["plain_text"], key)
        else:
            result = cipher.decrypt(request.form["cipher_text"], key)
    return render_template("transposition.html", result=result)


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2926, debug=True)
