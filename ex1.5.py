import timeit
import matplotlib.pyplot as plt

def func(n):
    if n in fib_cache:
        return fib_cache[n]
    elif n == 0 or n == 1:
        return n
    else: 
	    answer = func(n-1) + func(n-2) 

    fib_cache[n] = answer

    return answer

fib_cache = {}

def func_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return func_fib(n-1) + func_fib(n-2)

fib_mod_time = []

for i in range(0, 36):
    mod_time = timeit.timeit(lambda: func(i), number = 1, globals = None)
    fib_mod_time.append(mod_time)

fib_org_time = []
count = range(36)
j = 0

for i in range(0, 36):
    time_fib = timeit.timeit(lambda: func_fib(i), number = 1, globals = None)
    fib_org_time.append(time_fib)
    
plt.figure(1)
plt.plot(count, fib_org_time)
plt.ylabel("Time in seconds")
plt.xlabel("Range of fibonacci numbers")
plt.title("Memoization vs normal code to generate fibonacci numbers")
plt.plot(count, fib_mod_time)
plt.legend(["Original times", "Modified times"])
plt.show()