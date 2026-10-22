# Japanese Learning Backend

Backend API cho ứng dụng học tiếng Nhật, xây dựng bằng **Python + Flask**.

## 📋 Yêu cầu

- Python 3.10+
- pip
- Git

## 🚀 Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/<your-username>/japanese-learning.git
cd japanese-learning/backend
```

### 2. Tạo môi trường ảo

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Cài đặt dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements/dev.txt
```

### 4. Cấu hình biến môi trường

Tạo file `.env` từ file mẫu:

```bash
cp .env.example .env
```

Sau đó chỉnh sửa các giá trị trong `.env` cho phù hợp (database URL, secret key, ...).

### 5. Chạy ứng dụng

```bash
python -m flask --app wsgi run --debug
```

Ứng dụng sẽ chạy tại: **http://127.0.0.1:5000**

## 🗂️ Cấu trúc thư mục

```
backend/
├── app/
│   ├── core/                 # Cấu hình lõi, extensions, middleware
│   ├── modules/              # Các module nghiệp vụ
│   │   ├── auth/             # Xác thực & phân quyền
│   │   ├── users/            # Quản lý người dùng
│   │   ├── content/          # Nội dung học
│   │   ├── vocabulary/       # Từ vựng
│   │   ├── grammar/          # Ngữ pháp
│   │   ├── translation/      # Dịch thuật
│   │   ├── listening/        # Luyện nghe
│   │   ├── reading/          # Luyện đọc
│   │   ├── progress/         # Tiến độ học tập
│   │   ├── ai_assistant/     # Trợ lý AI
│   │   ├── billing/          # Thanh toán
│   │   │   └── gateways/     # Cổng thanh toán
│   │   └── community/        # Cộng đồng
│   ├── integrations/         # Tích hợp bên thứ ba
│   └── tasks/                # Background tasks
├── migrations/               # Database migrations
├── tests/                    # Unit & integration tests
│   ├── auth/
│   ├── vocabulary/
│   └── grammar/
├── scripts/                  # Script tiện ích
├── requirements/             # Danh sách dependencies
│   └── dev.txt
├── wsgi.py                   # Entry point cho WSGI server
└── README.md
```

## 🧪 Chạy tests

```bash
python -m pytest
```

Chạy một nhóm test cụ thể:

```bash
python -m pytest tests/auth
python -m pytest tests/vocabulary
python -m pytest tests/grammar
```

## 🛠️ Công nghệ sử dụng

- **Flask** — Web framework
- **SQLAlchemy** — ORM
- **Alembic** — Database migrations
- **Pytest** — Testing framework
- **Python-dotenv** — Quản lý biến môi trường

## 🤝 Đóng góp

1. Fork repository
2. Tạo branch mới: `git checkout -b feature/ten-tinh-nang`
3. Commit thay đổi: `git commit -m "Thêm tính năng ..."`
4. Push lên branch: `git push origin feature/ten-tinh-nang`
5. Tạo Pull Request

## 📄 License

MIT License — xem file [LICENSE](LICENSE) để biết chi tiết.