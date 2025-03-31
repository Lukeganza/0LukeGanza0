# download_music.py
import yt_dlp
import re  # Import thư viện để sử dụng regex

def download_music(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Đặt tên file tải về
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = info_dict['title']
        
        # Loại bỏ các ký tự không hợp lệ
        sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)  # Thay thế bằng dấu gạch dưới
        filename = f"{sanitized_title}.mp3"  # Tạo tên file mới

        return filename  # Trả về tên file tải xuống