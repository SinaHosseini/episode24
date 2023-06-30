from moviepy import editor
from time import time

if __name__ == "__main__":
    start = time()
    for i in range(1, 6):
        video = editor.VideoFileClip(f"vid/vid_{i}.mp4")
        video.audio.write_audiofile(f"aud/aud_{i}.mp3")

    end = time()
    print(end - start)