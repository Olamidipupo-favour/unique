#scraper.
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class unique(CrawlSpider):
    name="unique"
    start_urls=['http://localhost:80'] #will be changing it to wikipedia in the final release.
    nopes,denies,_ext=[],[],["png"]
    rules=(Rule(LinkExtractor(deny=nopes,deny_domains=denies,deny_extensions=_ext),callback='parse_item'),)
    def parse_item(self,response):
        item={}
        item['name']=response.xpath('//title/text()').extract()
        item['desc']=response.xpath('//body/text()').extract()[:10]
        item['url']=response.url
        print(item)
        en="mysql://dipo:dipo@localhost/dipo" #the engine.
        import sqlalchemy as s
        engine=s.create_engine(en,echo=True)
        metadata=s.MetaData()
        essential_info=s.Table(
    "webpage_info",
    metadata,
    s.Column("name",s.String),
    s.Column("desc",s.String(10)),
    s.Column("link",s.String)
)
        with engine.connect() as conn:
            result=conn.execute(s.insert(essential_info).values(name=item['name'],desc=item['desc'],url=item['url']))
            conn.commit()
            print("added")
        return item