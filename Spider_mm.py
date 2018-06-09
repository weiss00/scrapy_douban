# -*- coding:utf-8

import os

import urllib

import urllib2

from lxml import etree


class Spider:

    def __init__(self):

        self.tiebaName = raw_input('请输入需要访问的贴吧: ')
        self.beginPage = int(raw_input('请输入起始页: '))
        self.endPage = int(raw_input('请输入终止页: '))

        self.url = 'https://tieba.baidu.com/f'
        self.total_header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }

        self.image_number = 1

    # 访问用户选择的贴吧
    def spider_tieba(self):
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50

            word = {'pn' : pn, 'kw' : self.tiebaName}

            word = urllib.urlencode(word)

            my_url = self.url + '?' + word

            self.load_Page(my_url)


    # 加载页面
    def load_Page(self, url):
       # print '*'*20

        request = urllib2.Request(url)
        print url
        html = urllib2.urlopen(request).read()
        #print html
        #content = etree.HTML(html)
        #print content
        link_list = etree.HTML(html).xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        print link_list
        # for index in range(len(link_list)):
        #     if (index % 2) == 0:
        #         print(link_list[index].tag)
        #         print(link_list[index].attrib)
        #         print(link_list[index].text)
        # print link_list
        for link in link_list:

            link = 'https://tieba.baidu.com' + link

            self.load_Image(link)

    # 获取图片
    def load_Image(self, link):

        request = urllib2.Request(link, headers=self.total_header)
        html = urllib2.urlopen(request).read()
        content = etree.HTML(html)
        link_list = content.xpath('//img[@class="BDE_Image"]/@src')

        for links in link_list:
            self.write_Image(links)
    # 保存页面内容
    def write_Image(self, links):

        request = urllib2.Request(links, headers=self.total_header)
        image = urllib2.urlopen(request).read()
        filename = links[-9:]
        #os.mkdir('Image')
        #进入指定文件夹下载  图片便于管理
        os.chdir('C:\\Users\\lihaiyi.DESKTOP-338T55Q\\PycharmProjects\\Spider1\\Image')

        with open(filename, 'wb') as f:
            f.write(image)
        print "已经成功下载 " + filename

if __name__ == '__main__':

    mySpider = Spider()

    mySpider.spider_tieba()


