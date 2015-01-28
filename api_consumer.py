"""
 Base application to send data from external device to web service
 @author: Juan Carlos Delgado <jcdelgado@wtelecom.es>
"""

import urllib
import urllib2
import json
import settings

API_URL = "http://localhost:9000"

CONTENT_TYPE = {"Content-Type": "application/json"}

#  Dummy data 4 test
DUMMY = [{"key":1}, {"key":2}]

def makePath(path):
	# Return path without first slash if present
	baseurl = path
	if baseurl.startswith("/") > 0:
		baseurl = baseurl.replace("/","",1)

	return API_URL + "/" + baseurl


def postMeasureArray(data=[]):
	if type(data) is dict:
		data_array = [data]
	elif type(data) is list and len(data) > 0:
		data_array = data
	else:
		raise Exception("Invalid data submit", data)

	arguments = data_array

	try:
		json_arguments = json.dumps(arguments)
	except Exception, e:
		raise Exception("Fail to convert data to JSON", e)

	req = urllib2.Request(makePath('/api/send'), json_arguments, CONTENT_TYPE)
	req.add_header('Auth', 'basic-auth')

	request = urllib2.urlopen(req)
	read = request.read()

	if settings.DEBUG:
		print "=== READ HTTP RESPONSE ==="
		print read
		print "=========================="