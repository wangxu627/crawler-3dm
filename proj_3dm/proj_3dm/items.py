# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Proj3DmItem(scrapy.Item):
    # define the fields for your item here like:
    images = scrapy.Field()
    img_url = scrapy.Field()
    item_url = scrapy.Field()
    name = scrapy.Field()
