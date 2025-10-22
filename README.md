# 🧩 YouTube Playlist Downloader

Dự án này cho phép **tải toàn bộ playlist YouTube hoặc video đơn lẻ** bằng Python sử dụng thư viện **`yt-dlp`**.  
Hỗ trợ đầy đủ tính năng:  

✅ Tải playlist hoặc video riêng lẻ  
✅ Đăng nhập bằng **cookie** để tải video riêng tư / tránh giới hạn  
✅ Tự động gộp **video + audio** bằng `ffmpeg`  
✅ Tùy chọn định dạng đầu ra (`.mp4`, `.mkv`, v.v.)  
✅ Tự động tạo thư mục theo tên playlist  

> ⚠️ **Lưu ý:**  
> File `cookies.txt` **đã có sẵn trong folder dự án** và **không được chia sẻ công khai** vì chứa token đăng nhập.  

---

## ⚙️ 1. Yêu cầu hệ thống

### 🔹 Python
- Yêu cầu: **Python 3.8+**  
- Kiểm tra:
  ```bash
  python --version
  ```

### 🔹 Thư viện Python
- Cài đặt `yt-dlp`:
  ```bash
  pip install -U yt-dlp
  ```

### 🔹 FFmpeg
`yt-dlp` cần **ffmpeg** để hợp nhất video và audio.

#### 🪟 Trên Windows:
1. Tải bản full từ:  
   👉 [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Giải nén → copy thư mục `bin` vào:
   ```
   C:\Program Files\ffmpeg
   ```
3. Thêm đường dẫn sau vào **PATH**:
   ```
   C:\Program Files\ffmpeg\bin
   ```
4. Kiểm tra:
   ```bash
   ffmpeg -version
   ```

---

## 🍪 2. Xuất cookie từ trình duyệt (nếu playlist riêng tư)

1. Cài tiện ích Chrome:  
   👉 [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/)
2. Đăng nhập YouTube bằng tài khoản có quyền xem playlist.  
3. Mở tiện ích → chọn **Export cookies for youtube.com**  
4. Lưu file, ví dụ:
   ```
   D:\Hoc AI\Craw_YouTube\cookies.txt
   ```

> ⚠️ Không chia sẻ file này. Nếu hết hạn, export lại từ trình duyệt.

---

## 🧠 3. Cấu trúc dự án

```
Craw_YouTube/
│
├── download_playlist.py   # Script tải playlist
├── cookies.txt             # Cookie đăng nhập (nếu cần)
└── README.md               # File hướng dẫn này
```

---

## 🚀 4. Khởi tạo dự án (PowerShell hướng dẫn chi tiết)

> Copy toàn bộ khối lệnh bên dưới và dán vào PowerShell (chạy với quyền người dùng bình thường là đủ).

```powershell
# ---------- KHỞI TẠO DỰ ÁN ----------

# 1️⃣ Tạo thư mục dự án + nơi lưu video
New-Item -ItemType Directory -Path "D:\Hoc AI\Craw_YouTube" -Force
New-Item -ItemType Directory -Path "D:\YouTubeDownloads" -Force

# 2️⃣ Chuyển vào thư mục dự án
Set-Location -Path "D:\Hoc AI\Craw_YouTube"

# 3️⃣ (Tùy chọn) Cài FFmpeg qua winget (nếu chưa cài)
# Nếu không có winget, hãy cài thủ công từ trang gyan.dev
winget install -e --id Gyan.FFmpeg

# 4️⃣ Cài đặt yt-dlp
python -m pip install --upgrade pip
pip install -U yt-dlp

# 5️⃣ Đảm bảo file cookies.txt tồn tại (nếu playlist private)
#    D:\Hoc AI\Craw_YouTube\cookies.txt

# 6️⃣ Chạy script tải playlist (đã cấu hình URL bên trong script)
python download_playlist.py

# ---------- KẾT THÚC ---------- 
```

---

## 🧩 5. Gợi ý mở rộng
- Cho phép chọn định dạng tải (`best`, `mp4`, `mkv`)  
- Tự động đặt tên file theo tiêu đề video  
- Lưu log tải xuống (`download.log`)  
- Giao diện CLI để nhập URL playlist/video  

---

## 📄 Giấy phép
Dự án mang tính học tập cá nhân.  
Không được chia sẻ hoặc sử dụng cho mục đích vi phạm bản quyền nội dung YouTube.
