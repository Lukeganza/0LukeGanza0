from download_music import find_music_by_query, download_music
from playsound import playsound

# Chương trình chính
if __name__ == "__main__":
    api_key = "AIzaSyCbeNbC78nT-muobS-uW71S1J3FzSg0Lvg"  # API key của bạn
    search_query = input("Nhập từ khóa để tìm kiếm nhạc: ")

    # Tìm kiếm nhạc
    music_list = find_music_by_query(api_key, search_query)

    if music_list:
        print("Danh sách video tìm được:")
        for index, item in enumerate(music_list):
            if item['id']['kind'] == 'youtube#video':
                title = item['snippet']['title']
                description = item['snippet']['description']
                print(f"{index + 1}. {title} - {description}")

        choice = int(input("Nhập số thứ tự video bạn muốn tải (hoặc 0 để thoát): "))
        
        if 1 <= choice <= len(music_list):
            video_id = music_list[choice - 1]['id'].get('videoId')
            music_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"Tải nhạc từ URL: {music_url}")
            file_name = download_music(music_url)  # Gán tên tệp được trả về

            # Phát nhạc
            if file_name:  # Kiểm tra xem file_name có giá trị hợp lệ
                print(f"Đang phát nhạc {file_name}...")
                playsound(file_name)  # Phát tệp âm thanh
            else:
                print("Có lỗi xảy ra khi tải xuống tệp nhạc.")
        elif choice == 0:
            print("Thoát chương trình.")
        else:
            print("Lựa chọn không hợp lệ.")
    else:
        print("Không tìm thấy video nào để tải.")
