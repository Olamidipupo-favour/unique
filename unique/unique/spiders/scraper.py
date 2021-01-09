#scraper.
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import inito
class unique(CrawlSpider):
    name="unique"
    start_urls=['https://en.wikipedia.org/wiki/Main_Page','https://www.google.com','https://duckduckgo.com','https://facebook.com','http://crsso.ml'] #will be changing it to wikipedia in the final release.
    nopes,denies,_ext=[],[],["png",'jpg']
    rules=(Rule(LinkExtractor(deny=nopes,deny_domains=denies,deny_extensions=_ext),callback='parse_item'),)
    def parse_item(self,response):
        item=["","",""]
        item[0]=response.xpath('//title/text()').extract()[0]
        item[1]=response.xpath('//body/text()').extract()[:300][0].replace("\r","").replace("\n","").replace("\t","")
        item[2]=response.url
        print(item)
        db.child(child).push(item)
