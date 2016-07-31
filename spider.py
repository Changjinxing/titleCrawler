# coding: utf-8
from general import *
from bs4 import  BeautifulSoup,BeautifulStoneSoup
import urllib2
import html5lib
import sqlite3
from time import sleep, time
import gc

class Spider:
	# Class variables (shared among all instances)
	queue_file = ''
	queue = []
	crawled = []

	def __init__(self, queue_file):
		Spider.queue_file = queue_file
		self.boot()

	@staticmethod
	def boot():
		Spider.queue = file_to_arr(Spider.queue_file)
		Spider.crawled = []

	@staticmethod
	def getTitle(url):
		try:
			resource = urllib2.urlopen(url)
			page = resource.read()
			soup = BeautifulSoup(page, "html5lib")
			if soup.title is None:
				return 'title is not exist'
			title = soup.title.string
			if title is None:
				return 'title is not exist'
			title = title.replace("'", '-')
			title = title.replace('"', '-')
			resource.close()
		except IOError:
			title = ('ERROR: invalid URL "%s"' % url)
		return title

	@staticmethod
	def update_db(db_path, table_name, id, url, title):
		sqlite_db = sqlite3.connect(db_path)
		sqlite_cu = sqlite_db.cursor()
		sql_str= "insert into " + table_name + " values(" + str(id) + ", '" + url + "', '" + title + "')"
		#print sql_str
		sqlite_cu.execute(sql_str)
		sqlite_db.commit()

	@staticmethod
	def crawl_page(thread_name, page_url, db_path, table_name):
		if page_url not in Spider.crawled:
			print(thread_name + ' now crawling ' + page_url)
			print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
			#Spider.filter_links(page_url)
			if page_url in Spider.crawled:
				Spider.queue.remove(page_url)
				return
			Spider.queue.remove(page_url)
			Spider.crawled.append(page_url)
			db_id = len(Spider.crawled)

			title = Spider.getTitle(page_url)
			Spider.update_db(db_path, table_name, db_id, page_url, title)

			if len(Spider.crawled) != 0 and len(Spider.crawled)%1000 == 0:
				sleep(60)
				Spider.free()
			return title

        @staticmethod
        def free():
                #del Spider.queue
                #del Spider.crawled
                gc.collect()

	@staticmethod
	def filter_links(links):
		for url in links:
			if url in Spider.queue:
				Spider.queue.remove
				continue
			if url in Spider.crawled:
				continue
			Spider.queue.append(url)
