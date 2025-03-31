# sentence commentws
import pygame
import os
import subprocess
import download_music

# Hàm tìm kiếm URL từ tên bài nhạc
def search_music(query):
    command = ['yt-dlp', '--get-url', 'ytsearch:' + query]  # Xây dựng lệnh tìm kiếm
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None

# Hàm để gợi ý video từ YouTube
def suggest_music(query):
    command = ['yt-dlp', '--flat-playlist', '--get-title', '--no-playlist', 'ytsearch10:' + query]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip().split("\n") if result.returncode == 0 else []

# Hàm phát nhạc
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

# Hàm chính
def main():
    while True:
        title = input("Nhập tên bài nhạc (hoặc 'exit' để thoát): ")
        if title.lower() == 'exit':
            break

        # Gợi ý bài nhạc
        print("Gợi ý bài nhạc:")
        suggestions = suggest_music(title)
        for index, suggestion in enumerate(suggestions):
            print(f"{index + 1}: {suggestion}")

        choice = input("Chọn số gợi ý (hoặc nhấn Enter để tiếp tục với tên đã nhập): ")
        if choice.isdigit() and 1 <= int(choice) <= len(suggestions):
            title = suggestions[int(choice) - 1]

        # Tìm và tải URL nhạc
        url = search_music(title)
        if not url:
            print("Không tìm thấy bài nhạc.")
            continue

        # Tải nhạc và phát
        filename = download_music.download_music(url)
        
        if filename is None:
            print("Không thể tải nhạc, thử lại với bài khác.")
            continue  # Nếu không tải được nhạc, quay lại vòng lặp

        print(f"Đã tải nhạc thành công: {filename}")

        # Phát nhạc
        play_music(filename)

if __name__ == "__main__":
    main()
