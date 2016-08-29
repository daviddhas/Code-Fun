'''
Generate Parentheses
====================
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

def generate_parantheses(n):

	res = [] 
	generate(res,"",n,0)
	return res

def generate(sampler,str,n,m):
	if n == 0 and m ==0:
		sampler.append(str)
		return 

	if m >0:
		generate(sampler,str+')',n,m-1)
	if n >0:
		generate(sampler,str+'(',n-1,m+1)

print generate_parantheses(3)