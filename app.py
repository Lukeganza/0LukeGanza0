from flask import Flask, render_template, request
import requests
import yt_dlp

app = Flask(__name__)

# API Key YouTube (hãy thay thế bằng API Key thực tế của bạn)
API_KEY = "AIzaSyCbeNbC78nT-muobS-uW71S1J3FzSg0Lvg"

def find_music_by_query(api_key, query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "maxResults": 5,
        "q": query,
        "type": "video",
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  
    else:
        print("Error:", response.text)
        return None

def get_audio_url(video_url):
    """Trả về link phát trực tiếp của file nhạc từ YouTube"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info['url'] if 'url' in info else None

@app.route('/')
def index():
    return render_template('index.html', video_results=[], success=False)

@app.route('/download', methods=['POST'])
def download():
    search_query = request.form['query']
    music_list = find_music_by_query(API_KEY, search_query)

    video_results = []
    if music_list and 'items' in music_list:
        for music in music_list['items']:
            if music['id']['kind'] == 'youtube#video':
                video_id = music['id'].get('videoId')
                title = music['snippet']['title']
                description = music['snippet']['description']
                thumbnail = music['snippet']['thumbnails']['default']['url']
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                audio_url = get_audio_url(video_url)  # Lấy link nhạc từ YouTube

                video_results.append({
                    "video_url": video_url,
                    "audio_url": audio_url,
                    "title": title,
                    "description": description,
                    "thumbnail": thumbnail,
                })

    return render_template('index.html', video_results=video_results, success=bool(video_results))

if __name__ == '__main__':
    app.run(debug=True)

