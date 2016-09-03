from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def classic_fib(n):
	if n<=2:
		return n
	else:
		return classic_fib(n-2) + classic_fib(n-1)


def memoized_fib(n,memo=[]):
	memo = {}
	if n in memo:
		return memo[n]
	else:
		if n <=2:
			memo[n]= n
			return n
		else:
			memo[n]=memoized_fib(n-1)+memoized_fib(n-2)
			return memo[n]



print memoized_fib(5)

print classic_fib(5)