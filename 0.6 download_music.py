import os
import subprocess
from flask import Flask, request, send_file, jsonify

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
    subprocess.run(command, check=True)
    
    # Lấy tên file mp3 đã tải
    for file in os.listdir(DOWNLOAD_FOLDER):
        if file.endswith(".mp3"):
            return os.path.join(DOWNLOAD_FOLDER, file)
    return None

@app.route("/download_mp3", methods=["POST"])
def download_mp3():
    data = request.get_json()
    video_url = data.get("video_url")
    
    if not video_url:
        return jsonify({"error": "Thiếu video_url"}), 400
    
    try:
        mp3_file = download_audio(video_url)
        if mp3_file:
            return send_file(mp3_file, as_attachment=True)
        else:
            return jsonify({"error": "Không tìm thấy file MP3"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
