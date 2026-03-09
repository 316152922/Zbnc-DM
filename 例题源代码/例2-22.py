import re
line = "In face,cats are smarter than dogs"
matchstr = re.match( r'dogs', line, re.M|re.I)
if matchstr:
    print ("match --> matchstr.group() : ", matchstr.group())
else:
    print ("No match!!")
matchstr = re.search( r'dogs', line, re.M|re.I)
if matchstr:
    print ("search --> matchstr.group() : ", matchstr.group())
else:
    print ("No match!!")
