scrapy crawl dmoz

#!/usr/nim/env/ python
#coding:utf-8
#time:2017/6/4
#athor:L.P

#######��֤windowsʱ����24Сʱ��#######
import os
import time
from datetime import timedelta,datetime
seconds_per_day = 24*60*60

curTime = datetime.now()	#����ʱ��
print cuurTime
desTime = curTime.replace(hour=6,minute=30,second =0,micrisecind=0)	#����ִ��ʱ��
delta =decTime - curTime
skipSeconds = delta.total+seconds()
print 'skipsecond:%d'%skipSeconds
#time.replace([hour[,minute[,second[,microsecond[,tzinfo]]]]]):����һ���µ�ʱ������ò���ָ����ʱ���֡��롢΢�����ԭ�ж����е����ԣ�ԭ�ж����ӱ��ֲ��䣩

time.sleep(skipSecond)
os.system(r"E:\txt27\shellbat.bat")