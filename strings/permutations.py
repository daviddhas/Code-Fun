def permutate(s,step=0):
	print step
	if step == len(s):
		print "".join(s)

	copy = [x for x in s]
	
	for i in range (step,len(s)):
	
		copy[step],copy[i]= copy[i],copy[step]
	
		permutate(copy,step+1)

permutate("abc")