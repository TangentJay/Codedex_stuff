#9/23/2025
#scuffed scraping N stuff


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


#custom spooder class
class spoders(CrawlSpider):
    name = 'scuffed_web'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://books.toscrape.com/' ]

    rules = (
     Rule(LinkExtractor(allow='catalogue/category')), 
     Rule(LinkExtractor(allow='catalogue', deny='category'), callback='parse_item')         



    )


    def parse_item(self, response):
        yield{ 

            'title': response.css('.product_main h1').get(),
            'price': response.css('.price_color::text').get(),
            'availability': response.css('.availabilty::text').get()
        }