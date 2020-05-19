# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class ScrappixPipeline:

    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        self.conn = sqlite3.connect('amazon_data.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS amazon_laptops""")
        self.cursor.execute("""CREATE TABLE amazon_laptops(
                    ITEM_NAME text,
                    PRICE int,
                    STOCK int,
                    IMAGE blob)""")

    def process_item(self, item, spider):
        self.store_data(item)
        return item

    def store_data(self, item):
        self.cursor.execute("""INSERT INTO amazon_laptops VALUES (?, ?, ?, ?)""", (
            item['item_name'][0],
            item['price'][0],
            item['stock'][0],
            item['image'][0]
        ))
        self.conn.commit()
