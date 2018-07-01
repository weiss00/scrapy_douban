# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanspiderSpider(scrapy.Spider):
	name = 'doubanspider'
	allowed_domains = ['movie.douban.com']
	url = 'https://movie.douban.com/top250?start='
	offset = 0
	start_urls = [url + str(offset)]

	def parse(self, response):
		
		item = DoubanItem()
		movies = response.xpath('//div[@class="info"]')

		for each in movies:

			item['title'] = each.xpath('.//a/span[@class="title"][1]/text()').extract()[0]
			bd = each.xpath('.//div[@class="bd"]/p/text()').extract()[0]
			item['bd'] = bd.replace('\n', "").replace('    ', '')
			quote = each.xpath('.//p[@class="quote"]/span/text()').extract()
			if len(quote) != 0:
				item['quote'] = quote[0]
			else:
				pass
			item['star'] = each.xpath('.//div[@class="star"]//span[2]/text()').extract()[0]
			
			yield item
		
		if self.offset < 225:
			self.offset += 25
			yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
		
