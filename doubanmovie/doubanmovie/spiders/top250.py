# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from doubanmovie.items import DoubanmovieItem
from scrapy.http import FormRequest
import re

class Top250Spider(CrawlSpider):
    name = "top250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['http://movie.douban.com/top250']
    rules = [
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*')), process_request='add_cookie'),
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')), callback='parse_item', process_request='add_cookie')
    ]

    cookies = {
        'bid':"3fIQ0fOG7K0",
        "viewed":"1481158",
        "ll":"108306",
        "pk_id.100001.4cf6":"24cb8b41e39bd0c8.1439189814.6.1439272377.1439269973.",
        "__utma":"223695111.833585157.1439189814.1439269973.1439272377.6",
        "__utmc":"223695111",
        "__utmz":"223695111.1439189814.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
        "__utmt":"1",
        "ap":"1",
        "__utma":"30149280.68446865.1438931353.1439272377.1439278558.10",
        "__utmb":"30149280.6.10.1439278558",
        "__utmc":"30149280",
        "__utmz":"30149280.1439199459.7.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic"
    }

    def add_cookie(self, request):
        return request.replace(cookies=self.cookies)

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta={'cookiejar': i}, cookies=self.cookies)

    def parse_item(self, response):
        sel = Selector(response)

        item = DoubanmovieItem()
        item['title'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['top_order'] = sel.xpath('//span[@class="top250-no"]/text()').extract()
        item['subject_id'] = re.findall(r'\d+', response.url)
        item['director'] = sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['scriptwriter'] = sel.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        item['actor'] = sel.xpath('//*[@id="info"]/span[3]/span[2]/a/text()').extract()
        item['category'] = sel.xpath('//*[@id="info"]/span[@property="v:genre"]/text()').extract()
        item['released_date'] = sel.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"]/text()').extract()
        item['score'] = sel.xpath('//strong[@property="v:average"]/text()').extract()
        item['introduce'] = response.xpath('//span[@property="v:summary"]/text()').extract()
        item['imdb'] = response.xpath('//div[@id="info"]').re(u'<span class="pl">IMDb链接:</span>\s<a href="(.*?)".*<br>')
        item['length'] = response.xpath('//span[@property="v:runtime"]/text()').extract()
        item['alias'] = sel.xpath('//div[@id="info"]').re(u'<span class="pl">又名:</span>(.*)<br>')
        item['language'] = sel.xpath('//div[@id="info"]').re(u'<span class="pl">语言:</span>(.*)<br>')
        item['area'] = sel.xpath('//div[@id="info"]').re(u'<span class="pl">制片国家/地区:</span>(.*)<br>')

        return item
