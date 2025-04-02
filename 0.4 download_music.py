import requests
import yt_dlp

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
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Tùy chọn để xác định tên tệp đầu ra
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        # Tạo tên tệp từ thông tin video
        title = info_dict['title']
        return f"{title}.mp3"  # Trả về tên tệp đã tải xuống
