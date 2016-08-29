lessthan20s=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen", "Eighteen", "Nineteen"]
Tens=["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
Thousands=["","Thousand","Million","Billion"]	

def numbernames(num):

	if num == 0:
		return "Zero"
		
	res = ""

	for i in range(0,len(Thousands)):
		
		if num%1000 !=0:
			res = helper(num%1000) + Thousands[i] + " " + res
			num/=1000

	return res.strip()


def helper(num):

	if num == 0:
		return ""
	elif num <20:
		return lessthan20s[num]+" "
	elif num <100:
		return Tens[num/10]+" "+helper(num%10)
	else:
		return lessthan20s[num/100] + " Hundred " +helper(num%100)



print numbernames(1234)