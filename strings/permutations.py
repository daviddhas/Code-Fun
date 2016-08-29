def to_string(l):
	return ''.join(l)

def permute(s,l,r):
	if l ==r:
		to_string(s)
	for i in range(l,r+1):
		s[i],s[r]=s[r],s[i]

s = "ABC"
l = [1,2,3]
print s
print to_string(s)
#print permute(s)