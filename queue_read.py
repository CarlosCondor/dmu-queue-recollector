import settings
from time import sleep

FILE_NAME = settings.QUEUE_FILE_NAME
READ_MODE = "r"
FILE_MODE = READ_MODE
READ_DELAY = 5

def readQueue():
	"""
	Read file and return Array of tuples (lines)
	"""
	f = open(FILE_NAME, FILE_MODE)
	lines = [getFormatedData(line) for line in f]
	len_lines = len(lines)
	if settings.DEBUG:
		print "======= QUEUE LINES ============"
		print lines
		print "================================"
	return lines, len_lines

def getFormatedData(line):
	"""
	Input: line "1111timestamp, value\n"
	Return 2 values: timestamp, measure
	"""
	formated_line = line.strip().replace(" ","")
	array_line = formated_line.split(",")
	timestamp = int(array_line[0])
	measure = array_line[1]
	return (timestamp, measure)

def removeLines(num):
	"""
	Remove <num> numbers of lines from start of the file
	"""
	lines = open(FILE_NAME).readlines()
	open(FILE_NAME, "w").writelines(lines[num:])	

while 1:
	lines, len_lines = readQueue()
	for t,m in lines:
		if settings.DEBUG:
			print "====== TRUE DATA OF A LINE ========"
			print "time:", t
			print "measure:", m
			print "==================================="

	# Remove read lines
	removeLines(len_lines)

	print;print;print;print
	sleep(READ_DELAY)
