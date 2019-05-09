# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class NewsFeedItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    pub_date = Field()