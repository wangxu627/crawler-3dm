# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter


class Proj3DmPipeline:
    def process_item(self, item, spider):
        print("fffffffffffffffffffffffff")
        return item


class ImgPipeline(ImagesPipeline):
    # 1.根据图片进行请求
    def get_media_requests(self, item, info):
        print("===============>>>>> :::: ", item)
        name = item['name']
        for idx, image in enumerate(item['images']):
            yield scrapy.Request(url=image, meta={'name': name + "_" + str(idx) + ".jpg"})
        yield scrapy.Request(url=item["img_url"], meta={'name': name + "_cover.jpg"})

    # 2.指定图片路径/名字
    def file_path(self, request, response=None, info=None, *, item=None):
        # 保存名字
        name = request.meta['name']
        return name

    # 3.将item传递给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item
