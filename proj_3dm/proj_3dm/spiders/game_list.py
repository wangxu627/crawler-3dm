import scrapy
import re

class GameListSpider(scrapy.Spider):
    name = 'game_list'
    allowed_domains = ['3dmgame.com']
    start_urls = ['https://dl.3dmgame.com/all_all_1_time/']

    def parse(self, response):
        item_list = response.css("ul.downllis > li")
        for item in item_list[2:]:
            img_url = item.css("img").attrib["data-original"]
            item_url = item.css("div.text > div.bt > a").attrib["href"]
            name = item.css("div.text > div.bt > a::text").get()
            custom_data = {
                'img_url': img_url,
                'item_url': item_url,
                'name': name,
            }
            yield scrapy.Request(item_url, callback=self.parse_child, meta=custom_data)    
        r = re.match("https://dl.3dmgame.com/all_all_(\d+)_time/", response.url)
        if r:
            next_page = int(r.group(1)) + 1
            next_url = f"https://dl.3dmgame.com/all_all_{next_page}_time/"
        yield scrapy.Request(next_url, callback=self.parse)
        
    def parse_child(self, response):
        images = response.css("div.large_box > ul > li img::attr(src)").getall()
        yield {
            "images": images,
            'img_url': response.meta["img_url"],
            'item_url': response.meta["item_url"],
            'name': response.meta["name"],
        }