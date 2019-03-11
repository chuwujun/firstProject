import scrapy


class getSpider(scrapy.Spider):
    name="getSpider"

    @property
    def start_urls(self):
        return [
        "https://github.com/shiyanlou?before=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories",
        "https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxNiswODowMM4FkpXb&tab=repositories",
        "https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxNjoxNzo1MyswODowMM4Bx3_0&tab=repositories",
        "https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yNFQxNTowMDoxNyswODowMM4BnPdj&tab=repositories"
        ]

#    def parse(self,response):
#        for i in response.css('li.col-12'):
#            yield {
#                'name': i.css('a::text').extract_first().strip(),
#                'update_time': i.css('relative-time::attr(datetime)').extract_first()
#            }
    def parse(self,response):
#        for one in response.xpath('//div[contains(@class, "col-9")]'):
        for one in response.xpath('//div[@class="col-9 d-inline-block"]'):
            yield {
                'name':one.xpath('.//h3/a/text()').extract_first().strip(),
                'update-time':one.xpath('.//relative-time/@datetime').extract_first()
            }
