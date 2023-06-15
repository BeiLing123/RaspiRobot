# coding: utf-8

import os
import time
import importlib,sys

importlib.reload(sys)


def playVoice(url):
    print (url)
    os.system('mpg123 "%s"'%url)

if __name__ == '__main__':
    url = '/home/pi/Music/星空.mp3'
    playVoice(url)