# coding: utf-8

import requests
import json

# 创建post函数
def robot(content):
	api = 'http://openapi.turingapi.com/openapi/api/v2'  # 图灵API V2.0接口地址
	# 创建post提交的数据
	data = {
		"perception": {
			"inputText": {
				"text": content # 询问的文本
			}
		},
		"userInfo": {
			'apiKey': '***', # 图灵的apikey
			'userId': 'robot'
		}
	}   
	jsondata = json.dumps(data) # 转化为json格式
	response = requests.post(api, data=jsondata) # 发起post请求 
	robot_res = json.loads(response.content) # 将返回的json数据解码
	results = robot_res["results"][0]['values']['text'] # 提取对话数据
	print ('机器人：' + results)

# 创建对话死循环
while True:
	content = input("我：")
	robot(content)
	

