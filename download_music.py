import requests
import yt_dlp
import os

def find_music_by_query(api_key, query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            return data['items']
        else:
            print("Không tìm thấy thông tin nhạc.")
            return None
    else:
        print(f"Lỗi khi gọi API: {response.status_code} - {response.text}")
        return None

def download_music(url):
    output_path = os.path.join(r"C:\Users\phamt\OneDrive\Desktop\sick_musics(music_downloader)\download\music")  # Đường dẫn mới
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,  # Đường dẫn tệp MP3
        'keepvideo': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Tải nhạc
        mp3_file_name = f"{output_path}.mp3"  # Tạo tên tệp hoàn chỉnh cho tệp mp3
        print(f"Tệp MP3 đã được lưu tại: {mp3_file_name}")  # In thông báo tệp đã lưu
        return mp3_file_name  # Trả về đường dẫn tệp hoàn chỉnh