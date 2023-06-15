# coding: utf-8
import time
import playVoice
import recordVoice
import enhenc
import yuyinshibie
import Turling
import yuyinhecheng
import playing
import weather
import news

# 获取token
tok = yuyinshibie.get_access_token()

# 播放开启语音
url = yuyinhecheng.yuyinhecheng_api(tok,'欢迎使用语音交互机器人')
playVoice.playVoice(url)

switch = True
while switch:
	# 开始录音	
	recordVoice.recordVoice()
	# 语音降噪
	enhenc.enhenc('/home/pi/voice.wav')
	# 语音识别
	info = yuyinshibie.asr_main('/home/pi/enhenc.wav',tok)
	print ('我：' + info)

	if '关闭'.encode("utf-8") in info.encode("utf-8"):
		while True:
			recordVoice.recordVoice()
			enhenc.enhenc('/home/pi/voice.wav')
			info = yuyinshibie.asr_main('/home/pi/enhenc.wav',tok)
			print ('我：' + info)
		if '开启'.encode("utf-8") in info.encode("utf-8"):
			break
		url = yuyinhecheng.yuyinhecheng_api(tok,'开启成功')
		playVoice.playVoice(url)

	elif '暂停'.encode("utf-8") in info.encode("utf-8"):
		url = yuyinhecheng.yuyinhecheng_api(tok,'开始暂停')
		playVoice.playVoice(url)
		time.sleep(10)
		url = yuyinhecheng.yuyinhecheng_api(tok,'暂停结束')
		playVoice.playVoice(url)
		continue

	elif '结束对话'.encode('utf-8') in info.encode('utf-8'):
		url = yuyinhecheng.yuyinhecheng_api(tok,'下次再见吧')
		playVoice.playVoice(url)
		break

	# if判断语音内容中有无关键字
	# 有关键字
	# 关键字-点播 进入语音点播功能
	elif '播放'.encode('utf-8') in info.encode('utf-8'):
		# 播放语音合成的语音结果-进入点播功能
		url = yuyinhecheng.yuyinhecheng_api(tok,'进入点播功能')
		playVoice.playVoice(url)
		# 进入循环 一直识别语音内容
		while True:
			recordVoice.recordVoice()
			enhenc.enhenc('/home/pi/voice.wav')
			info = yuyinshibie.asr_main('/home/pi/enhenc.wav',tok)
			print ('我：' + info)
			# 识别名称并播放
			playing.playing(info)
			# 识别到关键字-退出 退出循环
			if '退出'.encode('utf-8') in info.encode('utf-8'):
				break
		# 播放语音合成的语音结果-退出点播
		url = yuyinhecheng.yuyinhecheng_api(tok,'退出点播')
		playVoice.playVoice(url)
		continue

	# 关键字-天气 
	elif '天气查询'.encode('utf-8') in info.encode('utf-8'):
		# 开始天气查询
		url = yuyinhecheng.yuyinhecheng_api(tok,'请说出想要查询的城市名称')
		playVoice.playVoice(url)
		recordVoice.recordVoice()
		enhenc.enhenc('/home/pi/voice.wav')
		info = yuyinshibie.asr_main('/home/pi/enhenc.wav',tok)
		print ('我：' + info)
		tex = info
		weather.weather(tok,tex)
		continue

	# 关键字-新闻 
	elif '新闻播报'.encode('utf-8') in info.encode('utf-8'):
		# 开始新闻播报
		news.news(tok)
		continue

	# 无关键字
	# 开始语音对话 进入智能陪聊状态
	else:
		# 图灵回复
		tex = Turling.Tuling(info)
		# 语音合成
		url = yuyinhecheng.yuyinhecheng_api(tok,tex)
		# 语音播放
		playVoice.playVoice(url)
		time.sleep(0.5)