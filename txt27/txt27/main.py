# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'txt27'])

"""
#此代码可以单独作为json文件存储和csv文件存储启动使用
from scrapy import cmdline
cmdline.execute("scrapy crawl txt".split())

"""