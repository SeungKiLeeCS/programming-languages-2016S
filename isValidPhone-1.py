#!/usr/local/bin/python
# IMPORT libraries
import cgi
import json
import sys
import cgitb
import re
# ENABLE CGI stuff so that you may get ERROR msgs
cgitb.enable()
# The FIRST print statement MUST write a header followed by a blank line
print "Content-Type: text/json\n"
# SHOW Python Version - useful
#print "python version = " + sys.version
# Obtain any PARAMETERS passed in via GET or POST from cgi.FieldStorage
# Here create an Object that 'acts' like a Dictionary but is not
parmObj = cgi.FieldStorage() #GET the PARAMS
# Iterate over the incoming KEYS
for key in parmObj.keys():
	pass
# FIND a particular key and value

# Create a python dict and use json.dumps
data = {}

instring = str(parmObj.getvalue(key))
if len(instring) > 12 or len(instring) < 9:
    data['isValidPhone'] = False	
elif re.search('^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$', instring):
    data['isValidPhone'] = True
else:
    data['isValidPhone'] = False

# CONVERT dictionary to a json string
json_data = json.dumps(data)
# SEND back to client
print json_data