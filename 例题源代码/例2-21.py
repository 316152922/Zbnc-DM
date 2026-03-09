import re
line = 'In fact, cats are  smarter  than dogs'
result = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if result:
    print (' result.group() : ', result.group())
    print (' result.group(1) : ', result.group(1))
    print (' result.group(2) : ', result.group(2))
