import os
import time
import requests
import yuyinhecheng
import yuyinshibie
import importlib,sys

importlib.reload(sys)

tok = yuyinshibie.get_access_token()

# 爬取搜狗主页中的热词新闻
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://www.sogou.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}
params = (
    ('v', int(time.time() * 1000)),
)
response = requests.get('https://www.sogou.com/suggnew/hotwords', headers=headers, params=params)
news_encode = response.text.encode().decode('unicode-escape').replace("var sogou_top_words=[", '').replace("]",'').replace('"', '').split(',')

def news(tok):
    url = yuyinhecheng.yuyinhecheng_api(tok,'下面播报,今日新闻')
    os.system('mpg123 "%s"'%url)
    for index, new in enumerate(news_encode):    
        print(f"{index + 1} {new}")
        if index < 10:
            url = yuyinhecheng.yuyinhecheng_api(tok,'第' + str(index + 1))
            os.system('mpg123 "%s"'%url)
            # 将新闻文本中的空格替换为逗号 存在空格会导致播报中断 
            new = new.replace(" ",",")
            url = yuyinhecheng.yuyinhecheng_api(tok,new)
            os.system('mpg123 "%s"'%url)
            time.sleep(0.5)
        else:
            url = yuyinhecheng.yuyinhecheng_api(tok,'今日新闻,播报完毕')
            os.system('mpg123 "%s"'%url)
            break

if __name__ == '__main__':
    news(tok)