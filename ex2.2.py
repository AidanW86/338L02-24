import sys
import json
import timeit
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
        
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json", "r") as inF:
    content = json.load(inF)

sort_time = []
count = range(10)
for x in content:
    time_func1 = timeit.timeit(lambda: func1(x, 0, (len(x)-1)), number = 1, globals = None)
    sort_time.append(time_func1)

plt.figure(1)
plt.plot(count, sort_time)
plt.ylabel("Time in seconds")
plt.xlabel("Array numbers")
plt.title("Time taken to sort arrays")
plt.show()