# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


"""
class Txt27Pipeline(object):
    def process_item(self, item, spider):
        return item
"""
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.http import Request
#from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import os
from scrapy.pipelines.files import FilesPipeline

from logging import log

import json
import codecs

class Txt27jsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('TXT.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item,skipkey =True), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class Txt27imagesPipeline(ImagesPipeline):          #重写方法一定要在setting配置中启动管道！！
    def get_media_requests(self, item, info):   #下载图片，重写 get_media_requests() 方法，并对各个图片URL返回一个Request:
        print "get_media_requests"
        for image_url in item['image_urls']:
            yield Request(image_url,meta={'item':item})
            # 添加meta是为了下面重命名文件名使用

    def file_path(self, request, response=None, info=None):     #重写file_path方法，自定义图片名称，默认方法会将图片名称url转换为哈希值显示
        item = request.meta['item']     #通过上面的meta传递过来item
        image_guid = item['txt_name']+'.'+request.url.split('/')[-1].split('.')[-1]     #拼接图片名称。request.url.split('/')[-1].split('.')[-1]得到图片后缀jpg
        filename =u'full/{0}'.format(image_guid)
        return filename

class Txt27DownloadPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for download_url in item['download_url']:
            yield Request(download_url,meta={'item':item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        file_guid = item['txt_name']+'.'+request.url.split('/')[-1].split('.')[-1]
        filename =u'full/{0}'.format(file_guid)
        return filename

"""
   def item_completed(self, results, item, info):  # 这些请求将被管道处理，当它们完成下载后，结果将以2-元素的元组列表形式传送到 item_completed() 方法:
        print "item_completed"
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        return item

   def file_path(self, request, response=None, info=None):
        print "file_path"
        #item = request.meta['item']     #通过上面的meta传递过来item
        #index = request.meta['index']   #通过上面的index传递过来列表中当前下载图片的下标
        image_guid = request.url.split('/')[-1]
        #request.url.split('/')[-1].split('.')[-1]得到图片后缀jpg,png

        return '%s.jpg' % (image_guid)
"""


class Txt27mysqlPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls,settings):
            dbparams = dict(
                host=settings['MYSQL_HOST'],  # 读取settings中的配置
                db=settings['MYSQL_DBNAME'],
                user=settings['MYSQL_USER'],
                passwd=settings['MYSQL_PASSWD'],
                charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
                cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=False,
            )
            dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
            return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def _conditional_insert(self, tx, item):
        print item['txt_jj']
        sql = "insert into text (txt_name,txt_zz,web_url,download_url,txt_zt,txt_jj) values(%s,%s,%s,%s,%s,%s)"
        params = (item["txt_name"],item["txt_zz"],item["web_url"],item["download_url"],item["txt_zt"],item["txt_jj"])
        tx.execute(sql,params)

    def _handle_error(self, failue, item, spider):
        print failue
