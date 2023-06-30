from threading import Thread
from moviepy import editor
from time import time


def convert(i):
    videos[i].audio.write_audiofile(vid_list[i] + '.mp3')


def thread_convert():
    for i in range(len(vid_list)):
        videos.append(editor.VideoFileClip(vid_list[i] + '.mp4'))
        threads.append(Thread(target=convert, args=[i]))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start = time()

    vid_list = ["vid/vid_1", "vid/vid_2",
                "vid/vid_3", "vid/vid_4", "vid/vid_5"]
    threads = []
    videos = []

    thread_convert()

    end = time()

    print(end - start)
