# coding: utf-8
import sqlite3
from sys import argv

if len(argv) > 2:
        db_path = str(argv[1])
        table_name = str(argv[2])
else:
        db_path = raw_input('please input the sqlite db path: ')
        table_name = raw_input('please input the table_name: ')

cx = sqlite3.connect(db_path)

cu = cx.cursor()

#cu.execute('create table url_title_rel (id integer primary key,url_tag varchar(50),title_name varchar(100) UNIQUE)')

#cu.execute("insert into url_title_rel values(0, 'http://www.baidu.com', '百度一
下，你就知道')")
#cu.execute("insert into url_title_rel values(1, 'http://www.google.com', 'google')") 

sql_str = 'select * from ' + table_name
cu.execute(sql_str)
urls = cu.fetchall()

num_db = len(urls)
print "items' count in db is(contain EMPTY title): ", num_db

for url in urls:
        if "ERROR" in url[2]:
                urls.remove(url)

#print urls
num_db = len(urls)
print "items' count in db is(except EMPTY title): ", num_db

#cu.execute("update url_title_rel set")
cx.commit()
