import scrapy


class MovieItem(scrapy.Item):
    rank = scrapy.Field()  # 电影排名
    cover = scrapy.Field()  # 电影图片
    types = scrapy.Field()  # 电影类型
    regions = scrapy.Field()  # 区域
    title = scrapy.Field()  # 电影名称
    actor_count = scrapy.Field()  # 演员数量
    vote_count = scrapy.Field()  # 投票数量
    score = scrapy.Field()  # 评分
    actors = scrapy.Field()  # 演员信息
    release_date = scrapy.Field()  # 发行时间
