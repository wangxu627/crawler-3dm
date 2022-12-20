import scrapy
import re

class GameListAliSpider(scrapy.Spider):
    name = 'game_list_ali'
    allowed_domains = ['ali213.net']
    start_urls = ['https://down.ali213.net/new/index_1.html']

    def parse(self, response):
        item_list = response.css(".famous-ul > div.famous-li")
        for item in item_list:
            img_url = item.css("a.content-a > img").attrib.get("src") or item.css("a.content-a > img").attrib.get("data-original")
            item_url = item.css("a.content-a").attrib.get("href")
            name = item.css("div.game-name::text").get()

            custom_data = {
                'img_url': img_url,
                'item_url': item_url,
                'name': name,
            }
            yield scrapy.Request("https://down.ali213.net/" + item_url, callback=self.parse_child, meta=custom_data)
        # r = re.match("https://dl.3dmgame.com/all_all_(\d+)_time/", response.url)
        # if r:
        #     next_page = int(r.group(1)) + 1
        #     next_url = f"https://dl.3dmgame.com/all_all_{next_page}_time/"
        # yield scrapy.Request(next_url, callback=self.parse)

    def parse_child(self, response):
        images = [("https:" + image) for image in response.css("div.detail_body_con_bb_con_con > div.detail_body_con_jt_con_title > span > a::attr(href)").getall()]
        yield {
            'name': response.meta["name"],
            'img_url': response.meta["img_url"],
            'item_url': response.meta["item_url"],
            "images": images,
        }