from threading import Thread
from time import time
import requests


def download(url, name):
    result = requests.get(url)

    f = open(name, "wb")
    f.write(result.content)
    f.close()


download("")