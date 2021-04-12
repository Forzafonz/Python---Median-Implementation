from CustomHeap import CustomHeap
import random
import sys

Lmax = []
Lmin = []
maxHeap = CustomHeap(Lmax, False)
minHeap = CustomHeap(Lmin)
median = 0

with open(r"C:\Users\golub\Downloads\Median.txt") as f:
    for line in f:

        key = int(line.strip())

        if len(Lmax) == 0 or len(Lmin) == 0:
            minHeap.heap_insert(key)

        elif int(key) >= minHeap.array[0]:
            minHeap.heap_insert(key)

        elif int(key) <= maxHeap.array[0]:
            maxHeap.heap_insert(key)
        else:
            roll = random.choice([1, 2])
            if roll == 1:
                maxHeap.heap_insert(key)
            else:
                minHeap.heap_insert(key)

        if abs(len(minHeap.array) - len(maxHeap.array)) == 2:
            if len(minHeap.array) > len(maxHeap.array):
                key = minHeap.extract_top_key()
                maxHeap.heap_insert(key)
            else:
                key = maxHeap.extract_top_key()
                minHeap.heap_insert(key)

        if (len(minHeap.array) + len(maxHeap.array)) % 2 == 0:
            element = int((len(minHeap.array) + len(maxHeap.array))) / 2 - 1
        else:
            element = int((len(minHeap.array) + len(maxHeap.array) + 1)) / 2 - 1

        if element <= len(maxHeap.array) -1:
            median_number = maxHeap.array[0]
        else:
            median_number = minHeap.array[0]

        median += median_number


median = median % 10000

print(minHeap.array)
print("=================")
print(maxHeap.array)
print(median)
