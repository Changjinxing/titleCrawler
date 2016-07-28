# coding: utf-8
import csv

# Read a csv file and convert each line to arr items
def file_to_arr(file_name):
	reader = csv.reader(open(file_name, 'rb'))
	results = []
	for item in reader:
		url = "http://www." + item[1]
		#url = item[1]
		results.append(url)
	return results