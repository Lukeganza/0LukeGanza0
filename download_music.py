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
        'cookiefile': 'cookies.txt',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'X-YouTube-Client-Name': '1',
            'X-YouTube-Client-Version': '2.20210818.01.00',  # Đảm bảo rằng chuỗi được kết thúc đúng cách
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'Referer': 'https://www.youtube.com/',
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict['title']
            sanitized_title = re.sub(r'[<>:"/\\|?*]', '', title)  # Loại bỏ các ký tự không hợp lệ
            filename = f"{sanitized_title}.mp3"  # Đặt tên file mp3
            return filename
    except yt_dlp.utils.DownloadError as e:
        print(f"Có lỗi xảy ra khi tải nhạc: {str(e)}")
        return None
    except Exception as e:
        print(f"Có lỗi không xác định: {str(e)}")
        return None