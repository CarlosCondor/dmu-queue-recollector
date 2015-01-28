import settings
import time
from random import randint

FILE_NAME = settings.QUEUE_FILE_NAME

def writeLine(timestamp, measure):
	with open(FILE_NAME, "a") as file:
		file.write("%s,%s\n" % (timestamp, measure) )


# DEBUG PRUPOSES
while 1:
	time.sleep(1)

	timestamp = int(time.time())
	measure = randint(0,100)

	writeLine(timestamp, measure)
	if settings.DEBUG:
		print "==============="
		print "Writing line at %s" % timestamp
		print "Measure: %s" % measure
		print "==============="