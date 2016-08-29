def longestCommonPrefix(strs):
    prefix = '';
    # * is the unpacking operator, essential here
    for z in zip(*strs):
    	print z
        bag = set(z);
        print bag
        if len(bag) == 1:
            prefix += bag.pop();
        else:
            break;
    return prefix;


def lcp(strs):

	 	return reduce(single,strs)

def single(string1,string2):
	i=0
	while i<len(string1) and i <len(string2):
		if string1[i] == string2[i]:
			i = i+1
		else:
			break
	return string1[:i]

strs= ["abasdas","abs","abdsa"]
print longestCommonPrefix(strs)

print lcp(strs)