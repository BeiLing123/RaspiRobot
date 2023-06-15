# coding: utf-8

from aip import AipSpeech

APP_ID='***' # API ID
API_KEY='***' # API KEY
SECRET_KEY='***' # SECRET KEY

# 初始化语音识别客户端
client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
#客户端合成文本生成结果，vol-指定语速
result=client.synthesis(text='生活就像海洋，只有意志坚强的人，才能到达彼岸',options={'vol':5})
#生成语音格式文件
if not isinstance(result,dict):
	with open('1.mp3','wb') as f:
		f.write(result)
else:
	print(result)


	