import scrapy  # 导入设置模块
import json
import re
from .. import settings
import io
import requests
# from movie.items import MovieItem
from .. items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/j/chart/top_list?' \
                  'type=11&interval_id=100%3A90&action=&start=0&limit=20']  # Ajax加载路径
    # headers = {'User-Agent': movie.settings.USER_AGENT}  # 头信息
    headers = {'User-Agent': settings.USER_AGENT}  # 头信息

    def start_requests(self):  # 该函数定义需要爬取的初始链接并下载网页内容
        yield scrapy.Request(self.start_urls[0], headers=self.headers)  # 发送请求

    def get_cover(self, item, cover_url):  # 获取电影图片
        response = requests.get(cover_url)
        img_data = response.content  # 获取图片内容
        item['cover'] = io.BytesIO(img_data)

    def parse(self, response):
        movies = json.loads(response.body)  # 解析JSON数据
        if movies:  # 数据存在
            for movie in movies:  # 字典迭代
                item = MovieItem()  # 实例化Item对象
                item['rank'] = movie['rank']  # 获取电影排名
                item['types'] = movie['types']  # 获取电影类型
                item['regions'] = movie['regions']  # 获取电影区域
                item['title'] = movie['title']  # 获取电影名称
                item['release_date'] = movie['release_date']
                item['actor_count'] = movie['actor_count']
                item['vote_count'] = movie['vote_count']
                item['score'] = movie['score']
                item['actors'] = movie['actors']
                self.get_cover(item, movie['cover_url'])
                yield item  # 返回数据项
            # 如果movies存在数据则对下一页进行采集（模拟页面滚动触发机制）
            page_num = re.search(r'start=(\d+)', response.url).group(1)
            page_num = 'start=' + str(int(page_num) + 20)
            next_url = re.sub(r'start=\d+', page_num, response.url)
            yield scrapy.Request(next_url, headers=self.headers)
