import os
import subprocess
from flask import Flask, request, send_file, jsonify, url_for

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_audio(video_url):
    """Tải nhạc từ YouTube bằng yt-dlp."""
    output_path = os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s")
    command = [
        "yt-dlp", "--extract-audio", "--audio-format", "mp3",
        "--output", output_path, video_url
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return None, f"Error downloading audio: {str(e)}"
    
    # Lấy tên file mp3 đã tải
    for file in os.listdir(DOWNLOAD_FOLDER):
        if file.endswith(".mp3"):
            return os.path.join(DOWNLOAD_FOLDER, file), None
    return None, "Không tìm thấy file MP3"

@app.route("/download_mp3", methods=["POST"])
def download_mp3():
    data = request.get_json()
    video_url = data.get("video_url")
    
    if not video_url:
        return jsonify({"error": "Thiếu video_url"}), 400
    
    mp3_file, error = download_audio(video_url)
    if mp3_file:
        mp3_url = url_for('static', filename='downloads/' + os.path.basename(mp3_file))
        return jsonify({"mp3_url": mp3_url})
    else:
        return jsonify({"error": error}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)


