import re
import requests
f = open('source.txt', 'r')
html = f.read()
f.close()

pic_url = re.findall('img src="(.*?)" class="lessonimg"', html)
i = 0
for each in pic_url:
    print('now downloading:' + each)
    pic = requests.get(each)
    fb = open('pic/'+str(i)+'.jpg','wb')
    fb.write(pic.content)
    fb.close()
    i += 1


