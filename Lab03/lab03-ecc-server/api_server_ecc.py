import os
from flask import Flask, request, jsonify
import ecdsa

app = Flask(__name__)

KEY_DIR = "keys"
PRIVATE_KEY_PATH = os.path.join(KEY_DIR, "ecc_private_key.pem")
PUBLIC_KEY_PATH = os.path.join(KEY_DIR, "ecc_public_key.pem")

if not os.path.exists(KEY_DIR):
    os.makedirs(KEY_DIR)

@app.route("/api/ecc/generate_keys", methods=["POST"])
def generate_keys():
    try:
        # Sử dụng đường cong NIST256p (secp256r1)
        sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
        vk = sk.get_verifying_key()
        
        # Lưu khóa bí mật (signing key)
        with open(PRIVATE_KEY_PATH, "wb") as f:
            f.write(sk.to_pem())
            
        # Lưu khóa công khai (verifying key)
        with open(PUBLIC_KEY_PATH, "wb") as f:
            f.write(vk.to_pem())
            
        return jsonify({"message": "Tạo cặp khóa ECC thành công!"}), 200
    except Exception as e:
        return jsonify({"error": f"Lỗi khi tạo khóa ECC: {str(e)}"}), 500

def load_keys():
    if not os.path.exists(PUBLIC_KEY_PATH) or not os.path.exists(PRIVATE_KEY_PATH):
        raise FileNotFoundError("Không tìm thấy file khóa ECC. Vui lòng tạo khóa trước.")
        
    with open(PRIVATE_KEY_PATH, "rb") as f:
        sk = ecdsa.SigningKey.from_pem(f.read())
        
    with open(PUBLIC_KEY_PATH, "rb") as f:
        vk = ecdsa.VerifyingKey.from_pem(f.read())
        
    return sk, vk

@app.route("/api/ecc/sign", methods=["POST"])
def ecc_sign():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Tin nhắn để ký không được để trống"}), 400
        
    try:
        sk, _ = load_keys()
        signature = sk.sign(message.encode('utf-8'))
        return jsonify({"signature": signature.hex()})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Lỗi khi ký (ECC): {str(e)}"}), 500

@app.route("/api/ecc/verify", methods=["POST"])
def ecc_verify():
    data = request.get_json()
    message = data.get("message")
    signature_hex = data.get("signature")

    if not message or not signature_hex:
        return jsonify({"error": "Tin nhắn và chữ ký không được để trống"}), 400
        
    try:
        _, vk = load_keys()
        signature = bytes.fromhex(signature_hex)
        is_verified = vk.verify(signature, message.encode('utf-8'))
        return jsonify({"is_verified": is_verified})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ecdsa.keys.BadSignatureError:
        return jsonify({"is_verified": False, "reason": "Chữ ký không hợp lệ."})
    except Exception as e:
        return jsonify({"error": f"Lỗi khi xác thực (ECC): {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
