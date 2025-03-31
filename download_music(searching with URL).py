# download_music.py
import yt_dlp
import re  # Import library to use regex

def download_music(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Name the file use want to download
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = info_dict['title']
        
        # remove unidentifi characters
        sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)  # replace with underslash
        filename = f"{sanitized_title}.mp3"  # create a new file name

        return filename  # return file name and download