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

    def parse(self,response):
        for i in response.css('li.col-12'):
            yield {
                'name': i.css('a::text').extract_first().strip(),
                'update_time': i.css('relative-time::attr(datetime)').extract_first()
            }
