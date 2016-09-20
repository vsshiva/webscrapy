import hashlib
import base64
mystring = "123456"
print hashlib.md5( mystring ).hexdigest()

encoded = base64.b64encode(mystring)
print "shiva"
print encoded