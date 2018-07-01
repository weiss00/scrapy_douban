# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

from settings import USER_AGENTS
from settings import PROXIES

# 

class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        #print useragent
        request.headers.setdefault("User-Agent", useragent)
        
class RandomProxy(object):
    def process_request(self, request, spider):
        proxies = random.choice(PROXIES)
        #print proxies
        request.meta['proxies'] = proxies['post_style'] + proxies['ip_port']
        