def palindrome_substrings(s):
	
	result =set()

	for i,char in enumerate(s):
	
		start,end = i-1,i+1
		
		while start >=0 and end <len(s) and s[start]==s[end]:
			result.add(s[start:end+1])
			start-=1
			end+=1

		start,end = i,i+1

		while start>=0 and end < len(s) and s[start]==s[end]:
			result.add(s[start:end+1])
			start-=1
			end+=1

	return list(result)

s = 'aabbaa'

print palindrome_substrings(s)