#Queue

#------------Array-based Queue------------
class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        return self.data[self._front]

    def dequeue(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        answer = self.data[self._front]
        self.data[self._front] = None
        self._front = (self._front + 1) % len(self.data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self.data):
            self._resize(2 * len(self.data))
        avail = (self._front + self._size) % len(self.data)
        self.data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
    
    def print_q(self):
        print("front -> ", end='')
        n = len(self.data)
        for i in range(0,n):
            if i != n - 1 and self.data[i] != None:
                print(self.data[i], " - ", end='')
            elif self.data[i] != None:
                print(self.data[i])
        print(" <- rear")

#------------Array-based Queue 실행 코드------------
print("\n----Array-base Queue----\n")
q = ArrayQueue()
q.enqueue('apple')
q.enqueue('orange')
q.enqueue('cherry')
q.enqueue('pear')
print("사과, 오렌지, 체리, 배 삽입 후: \t", end='')
q.print_q()
q.dequeue()
print("dequeue한 후:\t\t", end='')
q.print_q()
q.dequeue()
print("dequeue한 후: \t\t", end='')
q.print_q()
print("first: ", q.first())
q.enqueue('grape')
print("포도 삽입 후:\t\t", end='')
q.print_q()

#----------Array-base Queue enqueue & dequeue time----------
print("\n----Array-base Queue enqueue & dequeue time----\n")

import time

ArrayQ = ArrayQueue()

enArray = {}
deArray = {}
enArray_avg = {}
deArray_avg = {}

k = 10
for j in range(0, 7):
    en_start_time = time.time()
    for i in range(0, k):
        ArrayQ.enqueue(i)
    en_end_time = time.time()
    enTime = en_end_time - en_start_time
    enArray[k] = enTime
    enArray_avg[k] = enTime / k
    
    de_start_time = time.time()
    for i in range(0, k):
        ArrayQ.dequeue()
    de_end_time = time.time()
    deTime = de_end_time - de_start_time
    deArray[k] = deTime
    deArray_avg[k] = deTime / k

    k = k * 10

print("enqueue: ", enArray, '\n',"dequeue: ", deArray)
print("Average\n enqueue: ", enArray_avg, '\n',"dequeue: ", deArray_avg)

#------------Linked list-based Queue------------
class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        #노드 초기값
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self._head._element
    
    def dequeue(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    #Queue 출력
    def print_q(self):
        print("front -> ", end='')
        p = self._head
        while p:
            if p._next != None:  #p가 마지막 요소가 아닐 때
                print(p._element, "-> ", end='')
            else:  #p가 마지막 요소일 때
                print(p._element, end='')
            p = p._next
        print(" <- rear")

#------------Linked list-based Queue 실행 코드------------
print("\n----Linked list-base Queue----\n")
order = LinkedQueue()
order.enqueue('burger')
order.enqueue('coke')
order.enqueue('pizza')
order.enqueue('chicken')
print("버거, 콜라, 피자, 치킨 삽입 후: \t", end='')
order.print_q()
order.dequeue()
print("dequeue한 후:\t\t", end='')
order.print_q()
order.dequeue()
print("dequeue한 후: \t\t", end='')
order.print_q()
print("first: ", order.first())
order.enqueue('beer')
print("맥주 삽입 후:\t\t", end='')
order.print_q()

#----------Linked list-base Queue enqueue & dequeue time----------
print("\n----Linked list-base Queue enqueue & dequeue time----\n")

linkedQ = LinkedQueue()

enLinked = {}
deLinked = {}
enLinked_avg = {}
deLinked_avg = {}

k = 10
for j in range(0, 7):
    enqueue_start_time = time.time()
    for i in range(0, k):
        linkedQ.enqueue(i)
    enqueue_end_time = time.time()
    enqueueTime = enqueue_end_time - enqueue_start_time
    enLinked[k] = enqueueTime
    enLinked_avg[k] = enqueueTime / k
    
    dequeue_start_time = time.time()
    for i in range(0, k):
        linkedQ.dequeue()
    dequeue_end_time = time.time()
    dequeueTime = dequeue_end_time - dequeue_start_time
    deLinked[k] = dequeueTime
    deLinked_avg[k] = dequeueTime / k

    k = k * 10

print("enqueue: ", enLinked, '\n',"dequeue: ", deLinked)
print("Average\n enqueue: ", enLinked_avg, '\n',"dequeue: ", deLinked_avg)