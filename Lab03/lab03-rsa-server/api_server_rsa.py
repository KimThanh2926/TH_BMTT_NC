import rsa
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

KEY_DIR = "keys"
PUBLIC_KEY_PATH = os.path.join(KEY_DIR, "publicKey.pem")
PRIVATE_KEY_PATH = os.path.join(KEY_DIR, "privateKey.pem")

if not os.path.exists(KEY_DIR):
    os.makedirs(KEY_DIR)

@app.route("/api/rsa/generate_keys", methods=["POST"])
def generate_keys():
    """Tạo cặp khóa Public và Private mới."""
    try:
        (publicKey, privateKey) = rsa.newkeys(2048)
        
        # Lưu public key
        with open(PUBLIC_KEY_PATH, "wb") as f:
            f.write(publicKey.save_pkcs1("PEM"))
            
        # Lưu private key
        with open(PRIVATE_KEY_PATH, "wb") as f:
            f.write(privateKey.save_pkcs1("PEM"))
            
        return jsonify({"message": "Tạo cặp khóa RSA thành công!"}), 200
    except Exception as e:
        return jsonify({"error": f"Lỗi khi tạo khóa: {str(e)}"}), 500

def load_keys():
    """Tải khóa từ các file .pem."""
    if not os.path.exists(PUBLIC_KEY_PATH) or not os.path.exists(PRIVATE_KEY_PATH):
        raise FileNotFoundError("Không tìm thấy file khóa. Vui lòng tạo khóa trước.")
        
    with open(PUBLIC_KEY_PATH, "rb") as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
        
    with open(PRIVATE_KEY_PATH, "rb") as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
        
    return publicKey, privateKey

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    """Mã hóa tin nhắn bằng public key."""
    data = request.get_json()
    message = data.get("message")
    
    if not message:
        return jsonify({"error": "Tin nhắn không được để trống"}), 400
        
    try:
        publicKey, _ = load_keys()
        encrypted_message = rsa.encrypt(message.encode('utf-8'), publicKey)
        return jsonify({"encrypted_message": encrypted_message.hex()})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Lỗi mã hóa: {str(e)}"}), 500

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    """Giải mã tin nhắn bằng private key."""
    data = request.get_json()
    encrypted_message_hex = data.get("encrypted_message")

    if not encrypted_message_hex:
        return jsonify({"error": "Tin nhắn mã hóa không được để trống"}), 400
        
    try:
        _, privateKey = load_keys()
        encrypted_message = bytes.fromhex(encrypted_message_hex)
        decrypted_message = rsa.decrypt(encrypted_message, privateKey).decode('utf-8')
        return jsonify({"decrypted_message": decrypted_message})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except rsa.pkcs1.DecryptionError:
        return jsonify({"error": "Giải mã thất bại. Có thể do khóa sai hoặc dữ liệu không hợp lệ."}), 400
    except Exception as e:
        return jsonify({"error": f"Lỗi giải mã: {str(e)}"}), 500

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign():
    """Ký vào một tin nhắn bằng private key."""
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Tin nhắn để ký không được để trống"}), 400
        
    try:
        _, privateKey = load_keys()
        signature = rsa.sign(message.encode('utf-8'), privateKey, 'SHA-256')
        return jsonify({"signature": signature.hex()})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Lỗi khi ký: {str(e)}"}), 500

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify():
    """Xác thực chữ ký bằng public key."""
    data = request.get_json()
    message = data.get("message")
    signature_hex = data.get("signature")

    if not message or not signature_hex:
        return jsonify({"error": "Tin nhắn và chữ ký không được để trống"}), 400
        
    try:
        publicKey, _ = load_keys()
        signature = bytes.fromhex(signature_hex)
        is_verified = rsa.verify(message.encode('utf-8'), signature, publicKey)
        return jsonify({"is_verified": is_verified == 'SHA-256'})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except rsa.pkcs1.VerificationError:
        return jsonify({"is_verified": False, "reason": "Xác thực thất bại."})
    except Exception as e:
        return jsonify({"error": f"Lỗi khi xác thực: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
