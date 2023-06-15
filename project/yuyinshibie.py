# coding: utf-8

import os
import json 
import base64 
import requests
import urllib.request
import importlib,sys

importlib.reload(sys)

# 获取Access Token
def get_access_token(): 
	url = 'https://openapi.baidu.com/oauth/2.0/token' #授权服务地址
	body = { 
		'grant_type':'client_credentials', # 固定值
		'client_id' :'***', # API KEY
		'client_secret':'***', # SECRET KEY
	}
	r = requests.post(url,data=body,verify=True)
	respond = json.loads(r.text)
	return respond['access_token']

def yuyinshibie_api(audio_data,token): 
	# 对语音数据进行base64编码
	speech_data = base64.b64encode(audio_data).decode('utf-8') 
	# 计算此语音数据的字节数
	speech_length = len(audio_data) 
	post_data = { 
		'format' : 'wav', # 语音文件的格式
		'rate' : 16000, # 采样率
		'channel' : 1, # 声道数
		'cuid' : 'B8-27-EB-BA-24-14', # 用户唯一标识
		'token' : token, # 获取到的[access_token]
		'speech' : speech_data, # 本地语音文件的二进制语音数据
		'len' : speech_length # 本地语音文件的的字节数
	}
	url = 'http://vop.baidu.com/server_api' # 短语音识别请求地址
	json_data = json.dumps(post_data).encode('utf-8')
	json_length = len(json_data)

	req = urllib.request.Request(url, data=json_data)
	req.add_header('Content-Type', 'application/json')
	req.add_header('Content-Length', json_length)

	resp = urllib.request.urlopen(req)
	resp = resp.read()
	resp_data = json.loads(resp.decode('utf-8'))
	if resp_data['err_no'] == 0:
		return resp_data['result']
	else:
		print (resp_data)
		return None

def asr_main(filename,tok): 
	try: 
		# 读取文件
		f = open(filename, 'rb') 
		audio_data = f.read() 
		f.close() 
		# 识别本地文件
		resp = yuyinshibie_api(audio_data,tok) 
		return resp[0] 
	except Exception as e: 
		print ('e:',e)
		return '识别失败'.encode('utf-8')

if __name__ == '__main__':
	tok = get_access_token()
	print ('开始录音')
	os.system('sudo arecord -D "plughw:1,0" -f S16_LE -r 16000 -d 5 -t wav voice.wav')
	result = asr_main('/home/pi/voice.wav',tok)
	print ('语音识别：' + result)