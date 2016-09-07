def generate_parantheses(n):
	if not n:
		return ""
	res = []
	left,right = n,n

	helper(left,right, "", res)
	return res

def helper(left,right,path,res):
	if right < left:
		return

	if right ==0 and left ==0:
		res.append(path)
		return

	if left:
		helper(left-1,right,path+"(",res)

	if right:
		helper(left,right-1,path+")",res)


n = 3
print generate_parantheses(n)