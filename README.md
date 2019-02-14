 scrapyspider
--------------

#爬虫目的：<br>
得到豆瓣国产电视剧中，按热度排序的电视剧的名字、评分、标签、年份等信息。<br>

#运行：<br>
*安装好必要库：scrapy、jsonpath<br>

*在settings.py所在的目录下打开终端运行以下代码就能输出相应的电影数据<br>
scrapy crawl douban_ajax -o douban_movie.csv

#参考了[WoodenRobot的scrapy教程]<br>
 https://woodenrobot.me/2017/04/09/Scrapy爬虫框架教程（四）-抓取AJAX异步加载网页/
