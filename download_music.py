import yt_dlp
import re

def download_music(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br'
        },
        'cookiefile': 'cookies.txt'  # Nếu bạn sử dụng cookie
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict['title']
            # Tạo tên file bằng cách loại bỏ các ký tự không hợp lệ
            sanitized_title = re.sub(r'[<>:"/\\|?*]', '', title)  # Loại bỏ các ký tự không hợp lệ
            filename = f"{sanitized_title}.mp3"  # Tạo tên file mới
            
            return filename  # Trả về tên file tải xuống
    except Exception as e:
        print(f"Có lỗi xảy ra khi tải nhạc: {str(e)}")
        return None  # Nếu có lỗi, trả về None