# -*- coding: utf-8 -*-

import scrapy
from txt27.items import Txt27Item
from scrapy.http import Request

class Txt27(scrapy.Spider):
    name = "txt27"
    allowed_domains = ["www.80txt.com"]  # 定义约束区域
    start_urls = ['http://www.80txt.com/sort/1.html']  # 此行可注释

    def start_requests(self):
        for i in range(0,3):     #循环，爬取页数,这里设置爬取的页数
            if i ==0:
                url = 'http://www.80txt.com/sort/0.html'
            else:
                url = 'http://www.80txt.com/sort/'+ str(i) + '.html'    #拼接链接
                yield Request(url,callback=self.parse_one)      #将拼接链接传到parse_one函数

    def parse_one(self, response):  # 解析主页面
        item = Txt27Item()
        item['txt_url'] = response.xpath('//div[@class="book_bg"]/a/@href').extract()  # 抓取到详细页面信息
        for url in item['txt_url']:
            yield Request(url, callback=self.prase_two)

    def prase_two(self, response):
        web_url = response.xpath('//div[@class="soft_info_r"]/li[12]/b[1]/a/@href').extract()
        for ie in web_url:
            url = 'http://www.80txt.com' + ie
            yield Request(url, callback=self.parseDownload)

    def parseDownload(self, response):
        item = Txt27Item()
        item['txt_name'] = ''.join(response.xpath('//*[@id="titlename"]/h1/text()').extract()).replace(' ','')
        item['txt_zz'] = response.xpath('//*[@id="titlename"]/div/span[1]/text()').extract()
        item['web_url'] = response.xpath('//*[@id="textbox"]/div[1]/a[3]/@href').extract()
        item['txt_jj'] = ''.join(response.xpath('//div[@class="infos_txt"]/text()').extract()).replace(u'\xa0',u'').replace('\n', '').replace('\r','')      #此版本清除\xa0即&nbsp需要使用u‘’进行解决，否则会出现字符问题
        item['txt_zt'] = ','.join(response.xpath('//div[@class="txt_info"]/span/text()').extract())
        item['download_url'] = response.xpath('//*[@id="textbox"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/a[2]/@href').extract()
        item['image_urls'] = response.xpath('//*[@id="author"]/div/img/@src').extract()
        yield item