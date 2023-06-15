# coding: utf-8

import requests
import json
import importlib,sys

importlib.reload(sys)

# 图灵回复
def Tuling(words):
	api = 'http://openapi.turingapi.com/openapi/api/v2' # 图灵API V2.0接口地址
	# 创建post提交的数据
	data = {
		'perception': {
			'inputText': {
				'text': words # 询问的文本
			}
		},
		'userInfo': {
			'apiKey': '***', # 图灵的apikey
			'userId': 'robot'
		}
	}
	jsondata = json.dumps(data)
	r = requests.post(api, data=jsondata)
	
	if r:
		date = json.loads(r.text)
		results = date['results'][0]['values']['text']
		print ('机器人：' + results)
		return results
	else:
		print ('对不起,未获取到回复信息')
		return False

if __name__ == '__main__':
	words = input("我：")
	Tuling(words)