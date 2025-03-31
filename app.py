# main.py
from download_music import download_music
import pygame  # Import pygame
import os

def main():
    url = input("Nhập URL bài nhạc bạn muốn tải: ")
    filename = download_music(url)
    print(f"Đã tải nhạc thành công: {filename}")

    # Tạo đường dẫn đầy đủ để phát nhạc
    full_path = os.path.join(os.getcwd(), filename)

    # Kiểm tra file có tồn tại không
    if not os.path.exists(full_path):
        print(f"File không tồn tại: {full_path}")
        return

    # Khởi động pygame
    pygame.mixer.init()
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()

    print("Đang phát nhạc...")

    # Đợi cho đến khi nhạc phát xong
    while pygame.mixer.music.get_busy():
        continue

    print("Phát nhạc xong!")

if __name__ == "__main__":
    main()

