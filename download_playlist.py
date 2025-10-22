# ============================================
# 📥 download_playlist.py
# Tải toàn bộ playlist YouTube (kèm video, phụ đề, thumbnail)
# Chạy: python download_playlist.py
# Yêu cầu: pip install yt-dlp
# ============================================

import os
from yt_dlp import YoutubeDL

# ====== 🔧 CẤU HÌNH ======
PLAYLIST_URL = "https://youtube.com/playlist?list=PLold8GcM18ivnLrCjaSGCsiegiVpBL7ul&si=MAoOZA_nW2TAzigt"  # 👉 Link playlist
SAVE_PATH = r"D:\Hoc AI\Craw_YouTube\YouTubeDownloads"  # 👉 Thư mục lưu video
COOKIES_PATH = r"D:\Hoc AI\Craw_YouTube\youtube.com_cookies.txt"  # 👉 File cookies nếu playlist riêng tư
MAX_HEIGHT = 1080  # 👉 Giới hạn độ phân giải (None nếu muốn tải full 4K)
# =========================

# Tạo thư mục nếu chưa có
os.makedirs(SAVE_PATH, exist_ok=True)

# Định dạng tải (chọn best video + best audio)
if MAX_HEIGHT:
    fmt = f"bestvideo[height<={MAX_HEIGHT}]+bestaudio/best[height<={MAX_HEIGHT}]"
else:
    fmt = "bestvideo+bestaudio/best"

# Cấu trúc tên file khi lưu
out_template = os.path.join(
    SAVE_PATH, "%(playlist_title)s", "%(playlist_index)s - %(title)s.%(ext)s"
)

# ⚙️ Cấu hình yt-dlp
ydl_opts = {
    "format": fmt,
    "outtmpl": out_template,
    "merge_output_format": "mkv",
    "cookies": COOKIES_PATH,
    "ignoreerrors": True,           # ✅ Bỏ qua video lỗi thay vì dừng toàn bộ
    "retries": 5,                   # ✅ Thử lại nếu lỗi mạng
    "continuedl": True,             # ✅ Tiếp tục tải nếu bị gián đoạn
    "writethumbnail": True,         # ✅ Lưu thumbnail
    "embedthumbnail": True,         # ✅ Nhúng thumbnail vào video
    "addmetadata": True,            # ✅ Giữ metadata
    "writesubtitles": True,         # ✅ Tải phụ đề (nếu có)
    "embedsubtitles": True,         # ✅ Nhúng phụ đề vào video
    "writeinfojson": True,          # ✅ Lưu metadata .json
    "noplaylist": False,            # ✅ Tải toàn bộ playlist
    "postprocessors": [
        {"key": "FFmpegVideoConvertor", "preferedformat": "mkv"},
    ],
    "progress_hooks": [             # ✅ In tiến trình tải
        lambda d: print(f"📀 Đang tải: {d.get('filename', '')}")
        if d["status"] == "downloading"
        else None
    ],
}

# ============================================
print("=== 🎬 BẮT ĐẦU TẢI PLAYLIST ===")
print(f"🔗 URL: {PLAYLIST_URL}")
print(f"💾 Lưu tại: {SAVE_PATH}\n")

try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([PLAYLIST_URL])
    print("\n✅ Hoàn tất tải playlist. Tất cả video đã được lưu ở dạng mkv.")
except Exception as e:
    print("\n❌ Lỗi khi tải:", str(e))
