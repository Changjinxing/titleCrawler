# coding: utf-8
import sqlite3

cx = sqlite3.connect("./test.db")

cu = cx.cursor()

#cu.execute('create table url_title_rel (id integer primary key,url_tag varchar(50),title_name varchar(100) UNIQUE)')

#cu.execute("insert into url_title_rel values(0, 'http://www.baidu.com', '百度一下，你就知道')")
#cu.execute("insert into url_title_rel values(1, 'http://www.google.com', 'google')") 

cu.execute("select * from url_title_rel")
print cu.fetchall()

#cu.execute("update url_title_rel set")
cx.commit()