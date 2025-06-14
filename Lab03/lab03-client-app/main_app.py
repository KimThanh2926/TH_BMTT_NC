import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.main_window_ui import Ui_MainWindow

API_CLASSIC_URL = "http://127.0.0.1:5000/api" 
API_RSA_URL = "http://127.0.0.1:5001/api"     
API_ECC_URL = "http://127.0.0.1:5002/api" 

class CipherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        # Cổ điển
        self.ui.caesar_btn_encrypt.clicked.connect(self.handle_caesar_encrypt)
        self.ui.caesar_btn_decrypt.clicked.connect(self.handle_caesar_decrypt)
        self.ui.vigenere_btn_encrypt.clicked.connect(self.handle_vigenere_encrypt)
        self.ui.vigenere_btn_decrypt.clicked.connect(self.handle_vigenere_decrypt)
        self.ui.railfence_btn_encrypt.clicked.connect(self.handle_railfence_encrypt)
        self.ui.railfence_btn_decrypt.clicked.connect(self.handle_railfence_decrypt)
        self.ui.playfair_btn_encrypt.clicked.connect(self.handle_playfair_encrypt)
        self.ui.playfair_btn_decrypt.clicked.connect(self.handle_playfair_decrypt)
        self.ui.transposition_btn_encrypt.clicked.connect(self.handle_transposition_encrypt)
        self.ui.transposition_btn_decrypt.clicked.connect(self.handle_transposition_decrypt)
        
        # RSA
        self.ui.rsa_btn_gen_keys.clicked.connect(self.handle_rsa_generate_keys)
        self.ui.rsa_btn_encrypt.clicked.connect(self.handle_rsa_encrypt)
        self.ui.rsa_btn_decrypt.clicked.connect(self.handle_rsa_decrypt)
        self.ui.rsa_btn_sign.clicked.connect(self.handle_rsa_sign)
        self.ui.rsa_btn_verify.clicked.connect(self.handle_rsa_verify)

        # ECC
        self.ui.ecc_btn_gen_keys.clicked.connect(self.handle_ecc_generate_keys)
        self.ui.ecc_btn_sign.clicked.connect(self.handle_ecc_sign)
        self.ui.ecc_btn_verify.clicked.connect(self.handle_ecc_verify)


    def show_message(self, title, message, icon=QMessageBox.Information):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def call_api(self, base_url, endpoint, payload, method='POST'):
        try:
            url = f"{base_url}/{endpoint}"
            if method.upper() == 'POST':
                response = requests.post(url, json=payload, timeout=15)
            elif method.upper() == 'GET':
                 response = requests.get(url, timeout=15)
            else:
                 self.show_message("Lỗi Lập Trình", f"Phương thức '{method}' không được hỗ trợ.", QMessageBox.Critical)
                 return None

            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            self.show_message("Lỗi Mạng", f"Server tại {base_url} không phản hồi (timeout).", QMessageBox.Critical)
            return None
        except requests.exceptions.RequestException as e:
            self.show_message("Lỗi Mạng", f"Không thể kết nối đến server API:\n{e}\n\nHãy đảm bảo bạn đã chạy server.", QMessageBox.Critical)
            return None

    # --- Các hàm xử lý cho mã hóa cổ điển ---
    def _handle_classic_cipher(self, cipher_name, action):
        try:
            plain_text_widget = getattr(self.ui, f"{cipher_name}_text_plain")
            cipher_text_widget = getattr(self.ui, f"{cipher_name}_text_cipher")
            key_widget = getattr(self.ui, f"{cipher_name}_line_key")
            key = key_widget.text()
            if not key:
                self.show_message("Lỗi đầu vào", "Vui lòng nhập khóa.", QMessageBox.Warning)
                return

            if action == 'encrypt':
                source_text = plain_text_widget.toPlainText()
                if not source_text:
                    self.show_message("Lỗi đầu vào", "Vui lòng nhập văn bản cần mã hóa.", QMessageBox.Warning)
                    return
                payload_key_text, result_key = "text", "encrypted_text"
            else:
                source_text = cipher_text_widget.toPlainText()
                if not source_text:
                    self.show_message("Lỗi đầu vào", "Vui lòng nhập văn bản cần giải mã.", QMessageBox.Warning)
                    return
                payload_key_text, result_key = "text", "decrypted_text"

            if cipher_name in ["caesar", "railfence"]:
                try: key_val = int(key)
                except ValueError:
                    self.show_message(f"Lỗi Khóa {cipher_name.capitalize()}", "Khóa phải là một số nguyên.", QMessageBox.Warning)
                    return
            elif cipher_name == "vigenere":
                if not any(c.isalpha() for c in key):
                    self.show_message("Lỗi Khóa Vigenere", "Khóa phải là một từ (chứa các chữ cái).", QMessageBox.Warning)
                    return
                key_val = key
            else: key_val = key

            payload = {payload_key_text: source_text, "key": key_val}
            result = self.call_api(API_CLASSIC_URL, f"{cipher_name}/{action}", payload)

            if result and result_key in result:
                if action == 'encrypt': cipher_text_widget.setPlainText(result[result_key])
                else: plain_text_widget.setPlainText(result[result_key])
            elif result and "error" in result: self.show_message("Lỗi API", result["error"], QMessageBox.Warning)
        except AttributeError:
             self.show_message("Lỗi Lập Trình", f"Không tìm thấy widget cho mã hóa '{cipher_name}'.", QMessageBox.Critical)

    def handle_caesar_encrypt(self): self._handle_classic_cipher('caesar', 'encrypt')
    def handle_caesar_decrypt(self): self._handle_classic_cipher('caesar', 'decrypt')
    def handle_vigenere_encrypt(self): self._handle_classic_cipher('vigenere', 'encrypt')
    def handle_vigenere_decrypt(self): self._handle_classic_cipher('vigenere', 'decrypt')
    def handle_railfence_encrypt(self): self._handle_classic_cipher('railfence', 'encrypt')
    def handle_railfence_decrypt(self): self._handle_classic_cipher('railfence', 'decrypt')
    def handle_playfair_encrypt(self): self._handle_classic_cipher('playfair', 'encrypt')
    def handle_playfair_decrypt(self): self._handle_classic_cipher('playfair', 'decrypt')
    def handle_transposition_encrypt(self): self._handle_classic_cipher('transposition', 'encrypt')
    def handle_transposition_decrypt(self): self._handle_classic_cipher('transposition', 'decrypt')
            
    # --- Các hàm xử lý cho RSA ---
    def handle_rsa_generate_keys(self):
        result = self.call_api(API_RSA_URL, "rsa/generate_keys", payload={}) 
        if result and "message" in result: self.show_message("Thành công", result["message"])
        elif result and "error" in result: self.show_message("Lỗi API", result["error"], QMessageBox.Warning)

    def handle_rsa_encrypt(self):
        text = self.ui.rsa_text_plain.toPlainText()
        if not text:
            self.show_message("Lỗi đầu vào", "Vui lòng nhập văn bản cần mã hóa.", QMessageBox.Warning)
            return
        payload = {"message": text}
        result = self.call_api(API_RSA_URL, "rsa/encrypt", payload)
        if result and "encrypted_message" in result:
            self.ui.rsa_text_cipher.setPlainText(result["encrypted_message"])
            self.show_message("Thành công", "Mã hóa tin nhắn thành công!")
        elif result and "error" in result: self.show_message("Lỗi Mã Hóa RSA", result["error"], QMessageBox.Warning)

    def handle_rsa_decrypt(self):
        text = self.ui.rsa_text_cipher.toPlainText()
        if not text:
            self.show_message("Lỗi đầu vào", "Vui lòng nhập văn bản đã mã hóa (dạng hex).", QMessageBox.Warning)
            return
        payload = {"encrypted_message": text}
        result = self.call_api(API_RSA_URL, "rsa/decrypt", payload)
        if result and "decrypted_message" in result:
            self.ui.rsa_text_plain.setPlainText(result["decrypted_message"])
            self.show_message("Thành công", "Giải mã tin nhắn thành công!")
        elif result and "error" in result: self.show_message("Lỗi Giải Mã RSA", result["error"], QMessageBox.Warning)
            
    def handle_rsa_sign(self):
        text = self.ui.rsa_text_info.toPlainText()
        if not text:
            self.show_message("Lỗi đầu vào", "Vui lòng nhập thông điệp cần ký.", QMessageBox.Warning)
            return
        payload = {"message": text}
        result = self.call_api(API_RSA_URL, "rsa/sign", payload)
        if result and "signature" in result:
            self.ui.rsa_text_sign.setPlainText(result["signature"])
            self.show_message("Thành công", "Ký thông điệp thành công!")
        elif result and "error" in result: self.show_message("Lỗi Ký RSA", result["error"], QMessageBox.Warning)
            
    def handle_rsa_verify(self):
        message, signature = self.ui.rsa_text_info.toPlainText(), self.ui.rsa_text_sign.toPlainText()
        if not message or not signature:
            self.show_message("Lỗi đầu vào", "Vui lòng nhập thông điệp và chữ ký.", QMessageBox.Warning)
            return
        payload = {"message": message, "signature": signature}
        result = self.call_api(API_RSA_URL, "rsa/verify", payload)
        if result and "error" not in result:
            if result.get("is_verified", False): self.show_message("Thành công", "Chữ ký hợp lệ!")
            else: self.show_message("Thất bại", "Chữ ký không hợp lệ!", QMessageBox.Warning)
        elif result and "error" in result: self.show_message("Lỗi Xác thực RSA", result["error"], QMessageBox.Warning)

    # --- Các hàm xử lý cho ECC ---
    def handle_ecc_generate_keys(self):
        result = self.call_api(API_ECC_URL, "ecc/generate_keys", payload={})
        if result and "message" in result:
            self.show_message("Thành công", result["message"])
        elif result and "error" in result:
            self.show_message("Lỗi API", result["error"], QMessageBox.Warning)

    def handle_ecc_sign(self):
        text = self.ui.ecc_text_info.toPlainText()
        if not text:
            self.show_message("Lỗi đầu vào", "Vui lòng nhập thông điệp cần ký.", QMessageBox.Warning)
            return
        payload = {"message": text}
        result = self.call_api(API_ECC_URL, "ecc/sign", payload)
        if result and "signature" in result:
            self.ui.ecc_text_sign.setPlainText(result["signature"])
            self.show_message("Thành công", "Ký thông điệp (ECC) thành công!")
        elif result and "error" in result:
            self.show_message("Lỗi Ký ECC", result["error"], QMessageBox.Warning)

    def handle_ecc_verify(self):
        message, signature = self.ui.ecc_text_info.toPlainText(), self.ui.ecc_text_sign.toPlainText()
        if not message or not signature:
            self.show_message("Lỗi đầu vào", "Vui lòng nhập thông điệp và chữ ký.", QMessageBox.Warning)
            return
        payload = {"message": message, "signature": signature}
        result = self.call_api(API_ECC_URL, "ecc/verify", payload)
        if result and "error" not in result:
            if result.get("is_verified", False):
                self.show_message("Thành công", "Chữ ký ECC hợp lệ!")
            else:
                self.show_message("Thất bại", "Chữ ký ECC không hợp lệ!", QMessageBox.Warning)
        elif result and "error" in result:
            self.show_message("Lỗi Xác thực ECC", result["error"], QMessageBox.Warning)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CipherApp()
    window.show()
    sys.exit(app.exec_())
