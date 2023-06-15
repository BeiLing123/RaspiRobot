# coding: utf-8

import os
import time
import importlib,sys

importlib.reload(sys)

def recordVoice():
	print ('开始录音')
	os.system('sudo arecord -D "plughw:1,0" -f S16_LE -r 16000 -d 5 -t wav voice.wav')
	time.sleep(0.5)

if __name__ == '__main__':
	recordVoice()
