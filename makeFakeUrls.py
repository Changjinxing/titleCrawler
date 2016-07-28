
from general import *
from sys import argv

def main():
	if len(argv) > 3:
		filepath = str(argv[1])
		start_index = int(argv[2])
		write_cnt = int(argv[3])

	csvfile = file(filepath, 'wb')
	writer = csv.writer(csvfile)

	for i in range(start_index, write_cnt + 1):
	    url = [i,'http://www.baidu.com']
	    writer.writerow(url)
	print 'make fake urls done'


if __name__ == '__main__':
    main()