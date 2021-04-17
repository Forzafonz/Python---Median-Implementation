#For heaps:
# 0  1  2 3 4 5 6 7 8 9
#16 14 10 8 7 9 3 2 4 1   - keys of heap

#parent of node i: (i+1)//2. for node key 14: (1 + 1) //2 = 1, for node key 10: (2 + 1) // 2 = 1
#left node to node i: (2i + 1). for node key 14: (2+1) = 3, so 8
#right node to node i: 2i + 2: for node key 14: (2+2)  = 4, so 7
# left node to node key 8. Node key 8 i = 3, so left node = 2*3 + 1 = 7
# right node to node key 8. Node key 8 i = 3, so rigth node = 2*3 + 2 = 8
# right node to node key 10: 2*2 + 2 = 6
# left node to node key 7: 2 * i + 1 = 2 * 4 + 1 = 9
import sys


class CustomHeap():

    def __init__(self, array, htype = True):
        self.array = array
        self.htype = htype
        self.heapsize = len(array)

    def maxheapify(self, i):

        largest = i
        left_kid = 2*i + 1
        right_kid = 2*i + 2

        if left_kid <= len(self.array) -1:
            if self.array[left_kid] > self.array[largest]:
                largest = left_kid

        if right_kid <= len(self.array) - 1:
            if self.array[right_kid] > self.array[largest]:
                largest = right_kid

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.maxheapify(largest)

    def minheapify(self, i):

        smallest = i
        left_kid = 2*i + 1
        right_kid = 2*i + 2

        if left_kid <= len(self.array) - 1:
            if self.array[left_kid] < self.array[smallest]:
                smallest = left_kid

        if right_kid <= len(self.array) - 1:
            if self.array[right_kid] < self.array[smallest]:
                smallest = right_kid

        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.minheapify(smallest)

    def buildheap(self):

        # we only need to run max/min heapify for leafs of the heap
        for node in range(len(self.array)//2 - 1, -1, -1):
            if self.htype:
                self.minheapify(node)
            else:
                self.maxheapify(node)


    def heap_insert(self, key):

        if self.htype:
            self.array.append(sys.maxsize)
        else:
            self.array.append(-sys.maxsize)

        self.update_key(key, len(self.array) - 1)


    def update_key(self, key, i):

        if self.htype:
            if key < self.array[i]:
                self.array[i] = key
                while self.array[i] < self.array[(i-1)//2]:
                    if i == 0: break
                    self.array[i], self.array[(i-1)//2] = self.array[(i-1)//2], self.array[i]
                    i = (i-1)//2

        else:
            if key > self.array[i]:
                self.array[i] = key
                while self.array[i] > self.array[(i-1)//2]:
                    if i == 0: break
                    self.array[i], self.array[(i-1)//2] = self.array[(i-1)//2], self.array[i]
                    i = (i-1)//2

    def extract_top_key(self):

        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        key_extract = self.array.pop(-1)
        if self.htype:
            self.minheapify(0)
            #self.buildheap()
        else:
            self.maxheapify(0)
            #self.buildheap()
        return key_extract

# input array: [6,2,4,5,6,7,8,9,11,13,14]

if __name__ == '__main__':

    L = []
    heap = CustomHeap(L, False)

    L1 = []
    heap2 = CustomHeap(L1)
    print(heap2.array)
    with open(r"C:\Users\golub\Downloads\Median.txt") as f:

        for line in f:
            key = int(line.strip())
            heap.heap_insert(key)

    print(heap.array)
    heap.extract_top_key()
    print('===================================================')
    print(heap.array)