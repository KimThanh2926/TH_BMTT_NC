```markdown
# TH_BMTT__NC

## 📌 Môn học
Bảo Mật Thông Tin Nâng Cao (TH_BMTT__NC)

## 💻 Ngôn ngữ sử dụng
- Python (>= 3.11)

## 📝 Nội dung repo
Repo này chứa các bài thực hành về các thuật toán và kỹ thuật trong bảo mật thông tin:
- Mã hoá cổ điển: Caesar, Vigenère, Playfair, Railfence, Transposition
- Mã hoá hiện đại: AES + RSA
- Trao đổi khoá: Diffie-Hellman
- Hàm băm: MD5, SHA-256, SHA-3, Blake2
- WebSocket communication

## 📂 Cấu trúc thư mục
```

Lab02/
├── app.py
├── cipher/
│   ├── caesar/
│   ├── playfair/
│   ├── railfence/
│   ├── transposition/
│   ├── vigenere/
│   └── ...
├── templates/
└── ...

Lab04/
├── aes\_rsa\_socket/
├── dh\_key\_pair/
├── hash/
├── websocket/
└── server\_public\_key.pem

````

## ⚙ Cách cài đặt
```bash
# Clone repo
git clone https://github.com/KimThanh2926/TH_BMTT_NC.git
cd TH_BMTT_NC

# Cài đặt thư viện cần thiết (tuỳ Lab có thể cần cài riêng)
pip install -r Lab04/aes_rsa_socket/requirements.txt
pip install -r Lab04/dh_key_pair/requirements.txt
pip install -r Lab04/websocket/requirements.txt
````

## 🚀 Hướng dẫn chạy

Ví dụ:

```bash
# Chạy app Flask cho Lab02
python Lab02/app.py

# Chạy server AES + RSA
python Lab04/aes_rsa_socket/server.py

# Chạy client AES + RSA
python Lab04/aes_rsa_socket/client.py
```
## 👤 Tác giả
Kim Thanh Tran


---

