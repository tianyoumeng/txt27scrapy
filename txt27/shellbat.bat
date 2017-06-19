scrapy crawl dmoz

#!/usr/nim/env/ python
#coding:utf-8
#time:2017/6/4
#athor:L.P

#######保证windows时间是24小时制#######
import os
import time
from datetime import timedelta,datetime
seconds_per_day = 24*60*60

curTime = datetime.now()	#现在时刻
print cuurTime
desTime = curTime.replace(hour=6,minute=30,second =0,micrisecind=0)	#程序执行时刻
delta =decTime - curTime
skipSeconds = delta.total+seconds()
print 'skipsecond:%d'%skipSeconds
#time.replace([hour[,minute[,second[,microsecond[,tzinfo]]]]]):创建一个新的时间对象，用参数指定的时、分、秒、微妙代替原有对象中的属性（原有对象扔保持不变）

time.sleep(skipSecond)
os.system(r"E:\txt27\shellbat.bat")