def func(n):
    if n == 0 or n == 1:
        return n
    elif n in fib_cache:
        return fib_cache[n]
    else:
	    answer = func(n-1) + func(n-2)

    fib_cache[n] = answer

    return answer


fib_cache = {}