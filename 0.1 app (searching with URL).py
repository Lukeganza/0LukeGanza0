# main.py
from download_music import download_music
import pygame  # Import pygame
import os

def main():
    url = input("Type in song's URL: ")
    filename = download_music(url)
    print(f"Downloaded: {filename}")

    # created a link path to streams music
    full_path = os.path.join(os.getcwd(), filename)

    # check for file existence
    if not os.path.exists(full_path):
        print(f"File doesn't exist: {full_path}")
        return

    # run pygame
    pygame.mixer.init()
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()

    print("Playing...")

    # playing the music
    while pygame.mixer.music.get_busy():
        continue

    print("Done!")

if __name__ == "__main__":
    main()

