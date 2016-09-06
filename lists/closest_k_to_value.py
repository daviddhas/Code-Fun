def search(arr,x,l,size):
	mid = (l + size )/2

	if arr[mid]== x:
		return mid
	if arr[mid]<x:
		return search(arr,x,mid+1,size)
	if arr[mid]>x:
		return search(arr,x,l,mid)

def closest(arr,x,k):
	index = search(arr,x,0,len(arr)-1)
	l = index -1
	r = index+1
	res =[]
	count = 0
	while(l >=0 and r <len(arr) and count <=k):
		if x - arr[l] < arr[r]-x:
			res.append(arr[l])
			l-=1
			count+=1
		if x - arr[l] >x-arr[r]:
			res.append(arr[r])
			r+=1
			count+=1
	return res

l = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
x = 35
k =4
print closest(l,x,k)