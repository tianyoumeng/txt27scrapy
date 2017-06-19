# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Txt27Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    txt_name = scrapy.Field()  # 书名
    txt_zz = scrapy.Field()  # 作者
    txt_jj = scrapy.Field()  # 简介
    txt_url = scrapy.Field()  # 书籍url
    txt_zt = scrapy.Field()  # 书籍状态

    web_url = scrapy.Field()  # 书籍下载页面url
    download_url = scrapy.Field()  # 下载URL
    image_urls = scrapy.Field()  # 书籍封面URL
    images = scrapy.Field()     #根据images pipline管道，会把下载结果存储到images中
    files = scrapy.Field()      #根据files pipline管道，会把下载结果存储到files中
