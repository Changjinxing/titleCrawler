# titleCrawler
- Python multi-threaded website title crawler to crawl all the titles of websites
- using beautifulsoup4 + html5lib, you need install them on you system
	- pip install beautifulsoup4
	- pip install html5lib

- you need change the QUEUE_FILE_PATH, QUEUE_FILE_NAME and DB_FILE_PATH, DB_FILE_NAME to adjust your system in "main.py"
- you need change the sqlite table_name in "main.py"
- to run the crawler you should tap the command line like:

```
python main.py 
```
- you can also adjust you requirment to run the python background
- if you have any confusion about the titleCrawler


---
- add exception handling, you need keep in mind that the data never be nice when you crawling the real data or facing the read world. keep in mind. keep in mind. keep in mind.

---
- countValidCrawledTitles.py usage:
```
python countValidCrawledTitles.py db_path table_name
eq:
python countValidCrawledTitles.py test_db url_title_rel
```
- makeFakeUrls.py usage:
```
python makeFakeUrls.py filepath start_index write_cnt
eq:
python makeFakeUrls.py test.csv 1 100
```
- main.py usage(run in the background):
```
nice -n x nohup python main.py &
x is the number of the nice value, max is -20, min is 19
eq: 
nice -n -16 nohup python main.py &
you can trace the log dynamic by using: 
tail -f nohup.out
```

---
```
date: 2016/07/29
authour: zhangjinxing
email: jinxingbay@163.com
tell: 15600616254
```