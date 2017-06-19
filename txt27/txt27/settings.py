# -*- coding: utf-8 -*-

# Scrapy settings for txt27 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'txt27'

SPIDER_MODULES = ['txt27.spiders']
NEWSPIDER_MODULE = 'txt27.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30'
#scrapy默认的浏览器头是scrapy1.1 我们需要开启并且修改成伪装成浏览器头
#Mysql数据库的配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'txtdb'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = '123456'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用


IMAGES_STORE = 'E:\\txt27\\images'      #图片下载位置
FILES_STORE = 'E:\\txt27\\download'     #TXT小说文件下载格式

# 1 days of delay for files expiration     #设置文件过期时间，便于更新，保证管道不会下载未过期的文件
FILES_EXPIRES = 1               #单位是天

# 30 days of delay for images expiration    #设置小说图片过期时间，因为大部分小说封面更新时间比较长，所以设定时间久些
IMAGES_EXPIRES = 30

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'txt27 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True       #是否遵守robots.txt

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2      #下载延迟设置
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16        #线程并发数
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#这个是浏览器请求头，很多网站都会检查客户端的headers，比如豆瓣就是每一个请求都检查headers的user_agent，否则只会返回403，可以开启
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'txt27.middlewares.Txt27SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'txt27.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'txt27.pipelines.Txt27jsonPipeline': 300,
    'txt27.pipelines.Txt27mysqlPipeline': 300,
    'txt27.pipelines.Txt27imagesPipeline': 1,
    'txt27.pipelines.Txt27DownloadPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5       #开始下载时限速并延迟时间
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60        #高并发请求时最大延迟时间
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#最底下的几个：是否启用在本地缓存，如果开启会优先读取本地缓存，从而加快爬取速度，视情况而定
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
