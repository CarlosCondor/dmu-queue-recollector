import settings
from time import sleep

FILE_NAME = settings.QUEUE_FILE_NAME
READ_MODE = "r"
FILE_MODE = READ_MODE

def readQueue():
	f = open(FILE_NAME, FILE_MODE)
	lines = [line.strip().replace(" ","") for line in f]
	len_lines = len(lines)
	if settings.DEBUG:
		print "======= QUEUE LINES ============"
		print lines
		print "================================"
	return lines, len_lines

def getTrueData(line):
	"""
	Input: line ['1111timestamp','value']
	Return 2 values: timestamp, measure
	"""
	array_line = line.split(",")
	timestamp = int(array_line[0])
	measure = array_line[1]
	return timestamp, measure

def removeLines(num):
	lines = open(FILE_NAME).readlines()
	open(FILE_NAME, "w").writelines(lines[len_lines-1:-1])	

while 1:
	lines, len_lines = readQueue()
	for line in lines:
		t, m = getTrueData(line)
		if settings.DEBUG:
			print "====== TRUE DATA OF A LINE ========"
			print "time:", t
			print "measure:", m
			print "==================================="

	removeLines(len_lines)
	print;print;print;print
	sleep(5)