import re
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'}

html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search')

# print(html.text)


last_person = re.findall('title="最后回复人：(.*?)"',html.text,re.S)

for each in last_person:
    print(each)