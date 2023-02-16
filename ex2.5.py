import sys
import json
import timeit
import matplotlib.pyplot as plt

import random
# NOTE: the input was partially sorted. Making the input random improved the performance of the quicksort algorithm which is known perform poorly for nearly sorted inputs
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

def shuffle_arr(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def quickSort1( lists, OrderedLists, index):
    if len(lists) == 0:
        return OrderedLists
    
    UList = []
    LList =[]
    pivot = random.choice(lists)
    lists.remove(pivot)
    for i in lists:
        if i > pivot:
            UList.append(i)
        else:
            LList.append(i)
    OrderedLists[index + len(LList)] = pivot
    quickSort1(UList, OrderedLists, index + len(LList) + 1)
    quickSort1(LList,OrderedLists,index)
    
    return OrderedLists
    
with open("ex2.json", "r") as inF:
    content = json.load(inF)

sort_time = []
count = range(10)

sort_mod_time = []
for y in content:
    OrderedList= ['' for i in range(len(y))]
    time_mod_QS= timeit.timeit(lambda: quickSort1(y, OrderedList, 0), number = 1, globals = None)
    sort_mod_time.append(time_mod_QS)

for x in content:
    time_func1 = timeit.timeit(lambda: func1(x, 0, (len(x)-1)), number = 1, globals = None)
    sort_time.append(time_func1)

sort_time_Shuffle = []
shuffled_array = []
i =0
for z in content:
    random.shuffle(z)

    shuffled_array.append(z)
    time_shuffle = timeit.timeit(lambda: shuffle_arr(z, 0, (len(z)-1)), number = 1, globals = None)
    sort_time_Shuffle.append(time_shuffle)
    i = i + 1

with open("ex2.5.json", "w") as outfile:
    json.dump(shuffled_array,outfile)

plt.figure(1)
plt.plot(count, sort_time_Shuffle)
plt.ylabel("Time in seconds")
plt.xlabel("Array numbers")
plt.title("Time taken to sort arrays")
plt.show()