from lxml import etree
import requests
from multiprocessing.dummy import Pool as ThreadPool
import json



def writeTo(content):
    f.writelines('回帖时间:' + str(content["topic_reply_time"]) + "\n")
    f.writelines('回帖内容:' + str(content["topic_reply_content"]) + "\n")
    f.writelines('回帖人:'+str(content["user_name"])+"\n\n")

def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
        author = reply_info['author']['user_name']
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0]
        reply_time = reply_info['content']['date']
        item['topic_reply_time'] = reply_time
        item['topic_reply_content'] = content
        item['user_name'] = author
        writeTo(item)


if __name__ == "__main__":
    f = open('content.txt', 'a')
    pool = ThreadPool(4)
    page = []
    for i in range(1,21):
        newpage = 'http://tieba.baidu.com/p/4428720019?pn='+str(i)
        page.append(newpage)
    result = pool.map(spider,page)
    pool.close()
    pool.join()
    f.close()

