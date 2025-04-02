import pygame
import os
import subprocess
import download_music

def search_music(query):
    command = ['yt-dlp', '--get-url', 'ytsearch:' + query]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print("Không tìm thấy URL cho bài nhạc.")
        return None

def suggest_music(query):
    command = ['yt-dlp', '--flat-playlist', '--get-title', '--no-playlist', 'ytsearch10:' + query]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip().split("\n")
    else:
        print("Không thể gợi ý bài nhạc.")
        return []

def play_music(filename):
    full_path = os.path.join(os.getcwd(), filename)

    if not os.path.exists(full_path):
        print(f"File không tồn tại: {full_path}")
        return

    pygame.mixer.init()
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()
    
    print("Đang phát nhạc...")

    while pygame.mixer.music.get_busy():
        continue

    print("Phát nhạc xong!")

def main():
    while True:
        title = input("Nhập tên bài nhạc (hoặc 'exit' để thoát): ")
        if title.lower() == 'exit':
            break

        print("Gợi ý bài nhạc:")
        suggestions = suggest_music(title)
        if not suggestions:
            continue
        for index, suggestion in enumerate(suggestions):
            print(f"{index + 1}: {suggestion}")

        choice = input("Chọn số gợi ý (hoặc nhấn Enter để tiếp tục với tên đã nhập): ")
        if choice.isdigit() and 1 <= int(choice) <= len(suggestions):
            title = suggestions[int(choice) - 1]

        url = search_music(title)
        if not url:
            print("Không tìm thấy URL cho bài nhạc.")
            continue

        filename = download_music.download_music(url)
        
        if filename is None:
            print("Không thể tải nhạc, thử lại với bài khác.")
            continue
        
        print(f"Đã tải nhạc thành công: {filename}")
        play_music(filename)

if __name__ == "__main__":
    main()
