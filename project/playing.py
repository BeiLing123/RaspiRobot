# coding: utf-8

import os
import importlib,sys

importlib.reload(sys)

def playing(play):
    # 识别的文本中可能包含句号 如果有则去掉
    str1 = '。'
    if str1 in play:
        play = play[0 : len(play)-1]
    print (play)
    # 识别到名称 开始播放
    if play.encode('utf-8'):
        print ('播放中')
        os.system('mpg123 /home/pi/Music/'+ play + '.mp3')     

if __name__ == '__main__':
    play = input("请输入名称：")
    playing(play)