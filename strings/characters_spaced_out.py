def spaceout(s):
	dict = {}
	
	for i in s:
		dict[i]=dict.get(i,0)+1

	print dict
	res = "0"*len(s)
	s.sort()
	print s
	for i in sorted(dict.items(), key=lambda x: x[1],reverse = True):
		while i[1] >0:


	#print res

s = "labdabadi"

print spaceout(s)