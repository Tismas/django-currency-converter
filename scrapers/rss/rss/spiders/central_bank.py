# -*- coding: utf-8 -*-
import sqlite3

from lxml import etree
import scrapy

from xmlrpc.client import ServerProxy

class CentralBankSpider(scrapy.Spider):
    name = 'central_bank'
    allowed_domains = ['www.ecb.europa.eu']
    start_urls = ['https://www.ecb.europa.eu/home/html/rss.en.html']
    client = ServerProxy('http://localhost:8000/rpc/')

    def parse(self, response):
        for url in response.xpath('//ul[@class="zebraList"][2]/li/a/@href').extract():
            yield scrapy.Request('https://www.ecb.europa.eu' + url, callback=self.parse_xml)
    
    def parse_xml(self, response):
        parser = etree.XMLParser()
        root = etree.fromstring(response.body, parser)
        for entry in root.xpath('//*[local-name()="item"]'):
            base_currency = entry.xpath('.//*[local-name()="baseCurrency"]/text()')[0]
            target_currency = entry.xpath('.//*[local-name()="targetCurrency"]/text()')[0]
            value = entry.xpath('.//*[local-name()="value"]/text()')[0]
            date = entry.xpath('.//*[local-name()="date"]/text()')[0]
            date = date[:date.index('T')]

            self.client.add_exchange_rate(str(base_currency), str(target_currency), float(value), str(date))