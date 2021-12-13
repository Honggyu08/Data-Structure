#----------Selection Sort----------
def sel_sort(a):
    n =len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        tmp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = tmp

#----------Bubble Sort----------
def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp

#----------Quick Sort(Not in-place)----------
def quick_sort(a):
    if len(a) <= 1:
        return a
    
    pivot = len(a)//2
    lesser_arr = []
    equal_arr = []
    greater_arr = []

    for num in a:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    sorted = quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
    return sorted

#----------Quick Sort(In-place)----------
def partition(a, low, high):
    goUp = low + 1
    goDown = high

    while True:
        while goUp < high and a[goUp] < a[low]:
            goUp += 1
        while goDown > low and a[goDown] > a[low]:
            goDown -= 1
        if goDown <= goUp:
            break
        a[goUp], a[goDown] = a[goDown], a[goUp]
        goUp += 1
        goDown -= 1

    a[low], a[goDown] = a[goDown], a[low]
    return goDown

def quickSort(a, low, high):
    if  low < high:
        pivotIndex = partition(a, low, high)
        
        quickSort(a, low, pivotIndex - 1)
        quickSort(a, pivotIndex + 1, high)

#----------Merge Sort----------
def merge(a1, a2, a):
    i = j = 0
    while i + j < len(a):
        if j == len(a2) or ( i < len(a1) and a1[i] < a2[j]):
            a[i + j] = a1[i]
            i += 1
        else:
            a[i + j] = a2[j]
            j += 1

def merge_sort(a):
    n = len(a)
    if n < 2:
        return
    
    mid = n // 2
    a1 = a[0:mid]
    a2 = a[mid:n]

    merge_sort(a1)
    merge_sort(a2)

    merge(a1, a2, a)

#----------Radix Sort----------
def counting_sort(a, exp):
    n = len(a)
    max = 9
    count = [0] * (max + 1)
    output = [-1] * n

    for i in a:
        index = int((i/exp)%10)
        count[index] += 1

    for i in range(max):
        count[i + 1] += count[i]

    for i in range(n - 1, -1, -1):
        index = int((a[i]/exp)%10)
        output[count[index] - 1] = a[i]
        count[index] -= 1

    for i in range(0, n):
        a[i] = output[i]

def radix_sort(a):
    max1 = max(a)

    exp = 1
    while int(max1/exp) > 0:
        counting_sort(a, exp)
        exp *= 10

#----------Running time analysis----------
#Best case : already sorted
#퀵: 피봇을 가운데로
import time
import numpy as np

best = []
avg = []
worst = []

def initialize_arr():
    best1 = []
    best2 = []
    best3 = []

    for i in range(100):
        best1.append(i + 1)

    for i in range(200):
        best2.append(i + 1)

    for i in range(400):
        best3.append(i + 1)


    global best 
    best = [best1, best2, best3]

#average case (random 생성)
    avg1 = []
    avg2 = []
    avg3 = []

    avgT = np.random.randint(0, 100, (1, 100))
    avg1 = avgT[0]

    avgT = np.random.randint(0, 200, (1, 200))
    avg2 = avgT[0]

    avgT = np.random.randint(0, 400, (1, 400))
    avg3 = avgT[0]

    global avg
    avg = [avg1, avg2, avg3]

#worst case
    worst1 = []

    for i in range(100, 0, -1):
        worst1.append(i)

    worst2 = []

    for i in range(200, 0, -1):
        worst2.append(i)

    worst3 = []

    for i in range(400, 0, -1):
        worst3.append(i)

    global worst
    worst = [worst1, worst2, worst3]

sel_run = [[[], [], []], [[], [], []], [[], [], []]]
bubble_run = [[[], [], []], [[], [], []], [[], [], []]]
quick_run = [[[], [], []], [[], [], []], [[], [], []]]
quick_run_notIn = [[[], [], []], [[], [], []], [[], [], []]]
merge_run = [[[], [], []], [[], [], []], [[], [], []]]
radix_run = [[[], [], []], [[], [], []], [[], [], []]]

i = 0
initialize_arr()

#selection sort
for array in best:
    sel_start = time.time()
    sel_sort(array)
    sel_end = time.time()

    sel_time = sel_end - sel_start

    sel_run[0][i] = sel_time

    i += 1

i = 0
for array in avg:
    sel_start = time.time()
    sel_sort(array)
    sel_end = time.time()

    sel_time = sel_end - sel_start

    sel_run[1][i] = sel_time

    i += 1

i = 0
for array in worst:
    sel_start = time.time()
    sel_sort(array)
    sel_end = time.time()

    sel_time = sel_end - sel_start

    sel_run[2][i] = sel_time

    i += 1

initialize_arr()
i = 0

#bubble sort
for array in best:
    bubble_start = time.time()
    bubble_sort(array)
    bubble_end = time.time()

    bubble_time = bubble_end - bubble_start

    bubble_run[0][i] = bubble_time

    i += 1

i = 0
for array in avg:
    bubble_start = time.time()
    bubble_sort(array)
    bubble_end = time.time()

    bubble_time = bubble_end - bubble_start

    bubble_run[1][i] = bubble_time

    i += 1

i = 0
for array in worst:
    bubble_start = time.time()
    bubble_sort(array)
    bubble_end = time.time()

    bubble_time = bubble_end - bubble_start

    bubble_run[2][i] = bubble_time

    i += 1

initialize_arr()
i = 0

#quick sort
for array in best:
    quick_start = time.time()
    quickSort(array, 0, len(array)-1)
    quick_end = time.time()

    quick_time = quick_end - quick_start

    quick_run[0][i] = quick_time

    i += 1

i = 0
for array in avg:
    quick_start = time.time()
    quickSort(array, 0, len(array)-1)
    quick_end = time.time()

    quick_time = quick_end - quick_start

    quick_run[1][i] = quick_time

    i += 1

i = 0
for array in worst:
    quick_start = time.time()
    quickSort(array, 0, len(array)-1)
    quick_end = time.time()

    quick_time = quick_end - quick_start

    quick_run[2][i] = quick_time

    i += 1

initialize_arr()
i = 0

#quick sort not in-place
for array in best:
    quick_start_notIn = time.time()
    quick_sort(array)
    quick_end_notIn = time.time()

    quick_time_notIn = quick_end_notIn - quick_start_notIn

    quick_run_notIn[0][i] = quick_time_notIn

    i += 1

i = 0
for array in avg:
    quick_start_notIn = time.time()
    quick_sort(array)
    quick_end_notIn = time.time()

    quick_time_notIn = quick_end_notIn - quick_start_notIn

    quick_run_notIn[1][i] = quick_time_notIn

    i += 1

i = 0
for array in worst:
    quick_start_notIn = time.time()
    quick_sort(array)
    quick_end_notIn = time.time()

    quick_time_notIn = quick_end_notIn - quick_start_notIn

    quick_run_notIn[2][i] = quick_time_notIn

    i += 1

initialize_arr()
i = 0

#merge sort
for array in best:
    merge_start = time.time()
    merge_sort(array)
    merge_end = time.time()

    merge_time = merge_end - merge_start

    merge_run[0][i] = merge_time

    i += 1

i = 0
for array in avg:
    merge_start = time.time()
    merge_sort(array)
    merge_end = time.time()

    merge_time = merge_end - merge_start

    merge_run[1][i] = merge_time

    i += 1

i = 0
for array in worst:
    merge_start = time.time()
    merge_sort(array)
    merge_end = time.time()

    merge_time = merge_end - merge_start

    merge_run[2][i] = merge_time

    i += 1

initialize_arr()
i = 0

#radix sort
for array in best:
    radix_start = time.time()
    radix_sort(array)
    radix_end = time.time()

    radix_time = radix_end - radix_start

    radix_run[0][i] = radix_time

    i += 1

i = 0
for array in avg:
    radix_start = time.time()
    radix_sort(array)
    radix_end = time.time()

    radix_time = radix_end - radix_start

    radix_run[1][i] = radix_time

    i += 1

i = 0
for array in worst:
    radix_start = time.time()
    radix_sort(array)
    radix_end = time.time()

    radix_time = radix_end - radix_start

    radix_run[2][i] = radix_time

    i += 1


#----------동작 확인----------
array = [4, 6, 2, 7, 1, 3, 9, 10]
print("before:\n", array)
sel_sort(array)
print("selection:\n", array)

array = [4, 6, 2, 7, 1, 3, 9, 10]
print("before:\n", array)
bubble_sort(array)
print("bubble:\n", array)

array = [4, 6, 2, 7, 1, 3, 9, 10]
print("before:\n", array)
quickSort(array, 0, len(array)-1)
print("quick:\n", array)

array = [4, 6, 2, 7, 1, 3, 9, 10]
print("before:\n", array)
print("quick:\n", quick_sort(array))

array = [4, 6, 2, 7, 1, 3, 9, 10]
print("before:\n", array)
merge_sort(array)
print("merge:\n", array)

array = [4, 6, 2, 7, 1, 3, 9, 10]
print("before:\n", array)
radix_sort(array)
print("radix:\n", array)

#----------Result----------
print("----------Result----------")
print(sel_run)
print(bubble_run)
print(quick_run)
print(quick_run_notIn)
print(merge_run)
print(radix_run)