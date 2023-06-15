# coding: utf-8

import os
import time
import Turling
import yuyinshibie
import yuyinhecheng
import importlib,sys

importlib.reload(sys)

tok = yuyinshibie.get_access_token()

def weather(tok,tex):
	# 使用图灵天气预报的对话
	hour = time.localtime().tm_hour
	minute = time.localtime().tm_min
	tex = '现在是' + str(hour) + '点' + str(minute) +'分，下面是天气预报时间。' + Turling.Tuling(tex+'天气')
	# 如果有雨 提醒带雨伞
	if '雨' in tex:
		tex += '今天别忘记带雨伞哦！'
	# 播放最终的语音合成结果
	url = 'http://tsn.baidu.com/text2audio?tex='+tex+'&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok='+tok+'&per=0'
	os.system('mpg123 "%s"'%url)

if __name__ == '__main__':
	tex = input("请输入城市：")
	weather(tok,tex)