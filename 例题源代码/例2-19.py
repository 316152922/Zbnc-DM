se={23,32,-4,56,4,'a','m'}
for x in se:
	print(x,end=' ')
se.add('##')
se.discard(32)
print('\r')
for x in se:
	print(x,end=' ')
print('\n',se.pop())
print('\r',se)
