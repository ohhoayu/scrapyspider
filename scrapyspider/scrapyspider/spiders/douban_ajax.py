
import re
import json
import jsonpath

from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem
from urllib import parse


class DoubanAJAXSpider(Spider):
    name = 'douban_ajax'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }

    def start_requests(self):
        url='https://movie.douban.com/j/search_subjects?type=tv&tag=国产剧&sort=time&page_limit=20&page_start=0'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        jsonobj = json.loads(response.body)
        item = DoubanMovieItem()
        if jsonobj:
            citylist = jsonpath.jsonpath(jsonobj, '$..subjects')
            city = citylist[0]
            for i in range(len(city)):

                item['score'] = city[i]['id']
                idlist=item['score']
                
                url1='https://movie.douban.com/j/subject_abstract?subject_id='+str(idlist)
                yield Request(url1, headers=self.headers,callback=self.getInfo)
                
                yield item

            # 如果datas存在数据则对下一页进行采集
            page_num = re.search(r'page_start=(\d+)', response.url).group(1)
            page_num = 'page_start=' + str(int(page_num)+20)
            next_url = re.sub(r'page_start=\d+', page_num, response.url)

            url1='https://movie.douban.com/j/subject_abstract?subject_id='+str(idlist)
            yield Request(url1, headers=self.headers,callback=self.getInfo)
                
            yield Request(next_url, headers=self.headers)

    def getInfo(self, response):
        item = DoubanMovieItem()

        jsonobj = json.loads(response.body)
        yearlist = jsonpath.jsonpath(jsonobj, '$..release_year')
        labels=jsonpath.jsonpath(jsonobj, '$..types')
        nums= jsonpath.jsonpath(jsonobj, '$..id')
        title= jsonpath.jsonpath(jsonobj, '$..title')
        rate= jsonpath.jsonpath(jsonobj, '$..rate')
        
        item['score_num'] = yearlist
        item['labels']=labels
        item['nums']=nums
        item['title']=title
        item['rate']=rate
        yield item
