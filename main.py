# coding: utf-8
import threading
import Queue
from spider import Spider
from general import *
import sqlite3

# Choose the Project name
WORK_PATH = './'
DB_PATH = './'

QUEUE_FILE_NAME = 'top-1m.csv'
DB_FILE_NAME = 'test.db'

QUEUE_FILE_PATH = WORK_PATH + QUEUE_FILE_NAME

NUMBER_OF_THREADS = 8

DB_FILE_PATH = DB_PATH + DB_FILE_NAME

queue_links = file_to_arr(QUEUE_FILE_PATH)
queue = Queue.Queue()
Spider(queue_links)

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        table_name = 'url_title_rel'
        title = Spider.crawl_page(threading.current_thread().name, url, DB_FILE_PATH, table_name)
        #print title
        queue.task_done()

# Each queued link is a new job
def create_jobs():
    for link in queue_links:
        queue.put(link)
    queue.join()

# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = queue_links
    if len(queued_links) > 0:
        create_jobs()

# connect the sqlite db
sqlite_db = sqlite3.connect(DB_FILE_PATH)
sqlite_cu = sqlite_db.cursor()
table_name = 'url_title_rel'
sqlite_cu.execute('create table url_title_rel (id integer primary key,url_tag varchar(50),title_name varchar(100) UNIQUE)')

from time import clock
start_time = clock()
#print start_time
create_workers()
crawl()
finish_time = clock()
print finish_time
#print(finish_time - start_time)

#sqlite_cu.execute("select * from url_title_rel")
#print sqlite_cu.fetchall()