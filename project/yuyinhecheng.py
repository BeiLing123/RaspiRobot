# coding: utf-8

import os 
import json
import requests
import urllib.request 
import yuyinshibie
import importlib,sys

importlib.reload(sys)

def yuyinhecheng_api(tok,tex): 
	# 用户唯一标识 填写机器MAC地址或IMEI码
	cuid = 'B8-27-EB-BA-24-14' 
	# 语速 5为中语速
	spd = '4' 
	# GET调用方式拼接url
	url = 'http://tsn.baidu.com/text2audio?tex='+tex+'&lan=zh&cuid='+cuid+'&ctp=1&tok='+tok+'&per=0' 
	response = urllib.request.urlopen(url) 
	date = response.read() 
	return url

def tts_main(filename,words,tok): 
	voice_date = yuyinhecheng_api(tok,words)
	# 写入文件
	f = open(filename, 'wb')
	f.write(voice_date)
	f.close()

if __name__ == '__main__':
	tex = input("请输入文本：")
	tok = yuyinshibie.get_access_token()
	url = yuyinhecheng_api(tok,tex)
	os.system('mpg123 "%s"'%url)
