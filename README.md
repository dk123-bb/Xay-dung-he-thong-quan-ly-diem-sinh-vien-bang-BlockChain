<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
</h2>
<h2 align="center">
    PLATFORM ERP
</h2>
<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)
## 📌 Poster đề tài

![Poster đề tài](poster.png)
🎓 Hệ Thống Quản Lý Điểm Sinh Viên Bằng Blockchain

Hệ thống quản lý điểm sinh viên ứng dụng Blockchain + Smart Contract nhằm đảm bảo tính minh bạch, toàn vẹn và chống chỉnh sửa dữ liệu điểm số trong quá trình quản lý học tập.

📋 Tổng Quan Dự Án

Dự án là một hệ thống full-stack cho phép:

👨‍🏫 Giảng viên nhập và quản lý điểm sinh viên
👨‍🎓 Sinh viên xem điểm cá nhân và trạng thái xác thực
🔐 Blockchain lưu hash điểm để đảm bảo không thể sửa đổi
🗄️ Database MySQL lưu dữ liệu điểm chi tiết
⚖️ So sánh dữ liệu giữa Blockchain và Database để xác thực minh bạch

🏗️ Kiến Trúc Hệ Thống
Blockchain-Grading-System/
├── backend/        # Flask API + xử lý logic + Web3
├── blockchain/     # Smart Contract (Solidity - Hardhat)
└── frontend/       # Giao diện web (HTML / JS / Bootstrap)

⚙️ Công Nghệ Sử Dụng
🔗 Blockchain
Solidity (^0.8.x)
Hardhat
Ethereum / Ganache / Testnet
Web3 / Ethers.js
🖥️ Backend
Flask (Python)
MySQL Connector
Web3.py
hashlib (SHA-256)
🌐 Frontend
HTML / CSS / JavaScript
Bootstrap (UI dashboard)
AJAX / Fetch API

🔐 Cơ Chế Blockchain Trong Hệ Thống
Hệ thống hoạt động theo mô hình 2 lớp xác thực:

1. Lưu dữ liệu
Điểm sinh viên được lưu trong MySQL
Hệ thống tạo score_hash từ dữ liệu điểm
2. Ghi lên Blockchain
Hash được gửi lên Smart Contract
Blockchain lưu hash bất biến (immutable)
3. Xác thực dữ liệu
Khi kiểm tra:
So sánh hash MySQL ↔ hash Blockchain
Nếu giống → dữ liệu hợp lệ
Nếu khác → dữ liệu bị chỉnh sửa

🎯 Tính Năng Chính
👨‍🏫 Giảng viên
Thêm sinh viên
Nhập điểm
Cập nhật điểm
Tự động ghi hash lên blockchain
Kiểm tra tính toàn vẹn dữ liệu
👨‍🎓 Sinh viên
Đăng nhập hệ thống
Xem điểm cá nhân
Kiểm tra trạng thái xác thực điểm
Đảm bảo dữ liệu không bị sửa

🔐 Blockchain
Lưu hash điểm
Không thể chỉnh sửa dữ liệu
Minh bạch và công khai xác thực
Chống gian lận điểm số

📦 Cài Đặt & Chạy Dự Án
⚠️ Yêu cầu hệ thống
Node.js (v18+)
Python (3.8+)
MySQL
MetaMask (nếu dùng testnet)
🚀 1. Cài đặt dependencies
# Blockchain
cd blockchain
npm install

# Backend
cd ../backend
pip install -r requirements.txt

# Frontend
cd ../frontend
⛓️ 2. Deploy Smart Contract
Compile contract
cd blockchain
npx hardhat compile
Chạy local blockchain
npx hardhat node
Deploy contract
npx hardhat run scripts/deploy.js --network localhost

👉 Sau khi deploy:

Copy Contract Address
Copy ABI
🗄️ 3. Cấu hình Backend
Tạo file .env
RPC_URL=http://localhost:8545

PRIVATE_KEY=your_private_key_here

CONTRACT_ADDRESS=your_contract_address_here

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=student_score

PORT=5000
Copy ABI
copy blockchain\artifacts\contracts\*.json backend\
▶️ 4. Chạy Backend
cd backend
python app.py

Backend chạy tại:

http://localhost:5000
🌐 5. Chạy Frontend
cd frontend

Mở file:

index.html

hoặc dùng Live Server (VS Code)

📊 Cấu Trúc Database
students

| id | student_code | full_name |

scores

| id | student_id | score | score_hash |

🔧 Smart Contract Functions
📌 addScore(studentId, scoreHash)
Lưu hash điểm lên blockchain
📌 verifyScore(studentId, scoreHash)
Kiểm tra hash hợp lệ hay không
📌 updateScore(...)
Cập nhật hash mới (nếu được phép)

🔍 Kiểm Tra Hệ Thống
Backend: http://localhost:5000
Frontend: mở index.html
Blockchain: terminal Hardhat
Database: MySQL student_score
🐛 Troubleshooting
🔗 Lỗi kết nối blockchain
Kiểm tra RPC_URL
Kiểm tra Hardhat node đang chạy

🗄️ Lỗi MySQL
Kiểm tra database student_score
Kiểm tra user/password trong .env
⚙️ Lỗi Flask
Kiểm tra app.py
Kiểm tra port 5000
⛓️ Lỗi smart contract
Deploy lại contract
Kiểm tra ABI + address

🔐 Bảo Mật
❌ Không commit .env
❌ Không public private key
🔐 Dùng testnet / Ganache khi dev
💾 Backup ví blockchain

📌 Ưu Điểm Hệ Thống
✔️ Minh bạch dữ liệu điểm
✔️ Chống sửa điểm trái phép
✔️ Xác thực bằng Blockchain
✔️ Kết hợp Web2 + Web3
✔️ Phù hợp đồ án tốt nghiệp
