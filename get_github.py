import scrapy


class getSpider(scrapy.Spider):
    name="getSpider"
    @property
    def start_urls(self):
        url1="https://github.com/shiyanlou?before=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories"
        url2="https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxNiswODowMM4FkpXb&tab=repositories"
        url3="https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxNjoxNzo1MyswODowMM4Bx3_0&tab=repositories"
        url4="https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yNFQxNTowMDoxNyswODowMM4BnPdj&tab=repositories"
        return (url for url in [url1,url2,url3,url4])

    @property
    def parse(self,response):
        listb=response.xpath('//relative-time/@datetime').extract()
        lista=response.xpath('//h3/a/text()').re('\\n\s*(.*)')
        for one in lista:
            name=one
            update_time=listb[lista.index(one)]
            yield{"name":name,"update_time":update_time}
