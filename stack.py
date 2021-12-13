#Stack

#------------Array-based Stack------------
class ArrayStack:
    def __init__(self):
        self.data = []  #초기 상태

    #스택의 길이 반환
    def __len__(self):
        return len(self.data)

    #스택이 비어있는지 반환
    def isEmpty(self):
        return len(self.data) == 0

    #스택에 요소 push
    def push(self, e):
        self.data.append(e)

    #스택에서 가장 위의 요소 반환
    def top(self):
        if self.isEmpty():  #리스트가 비어있다면 다음 출력
            raise Empty('ArrayStack is empty')
        return self.data[-1]  #리스트에서 가장 마지막 요소 반환

    #스택에서 가장 위의 요소 삭제 및 반환
    def pop(self):
        if self.isEmpty():  #리스트가 비어있다면 다음 출력
            raise Empty('ArrayStack is empty')
        return self.data.pop()  #리스트의 가장 마지막 요소 삭제 및 반환
    
    def clear(self):
        self.data = []

#------------Array-base Stack 실행 코드------------
print("\n----Array-base Stack----\n")
fruit = ArrayStack()
fruit.push('apple')
fruit.push('orange')
fruit.push('cherry')
print("사과, 오렌지, 체리 push 후:\t", end='')
print(fruit.data, '\t<- top')
print("top 항목: ", end='')
print(fruit.top())
fruit.push('pear')
print("배 push 후:\t\t", end='')
print(fruit.data, '\t<- top')
fruit.pop()
fruit.push('grape')
print("pop(), 포도 push 후:\t", end='')
print(fruit.data, '\t<- top')

#----------Array-base Stack push & pop time----------
print("\n----Array-base Stack push & pop time----\n")

import time

ArrayStack = ArrayStack()

pushArray = {}  #input 개수를 key로 하고 총 push시간을 value로 하는 dictionary 생성
popArray = {}  #input 개수를 key로 하고 총 pop시간을 value로 하는 dictionary 생성
pushArray_avg = {}  #input 개수를 key로 하고 push의 평균시간을 value로 하는 dictionary 생성
popArray_avg = {}  #input 개수를 key로 하고 pop의 평균시간을 value로 하는 dictionary 생성

k = 10  #input의 초기 개수
for j in range(0, 7):
    push_start_time = time.time()  #push 시작 시간
    for i in range(0, k):
        ArrayStack.push(i)
    push_end_time = time.time()
    pushTime = push_end_time - push_start_time
    pushArray[k] = pushTime
    pushArray_avg[k] = pushTime / k
    
    pop_start_time = time.time()
    for i in range(0, k):
        ArrayStack.pop()
    pop_end_time = time.time()
    popTime = pop_end_time - pop_start_time
    popArray[k] = popTime
    popArray_avg[k] = popTime / k

    k = k * 10

print("push: ", pushArray, '\n',"pop: ", popArray)
print("Average\n push: ", pushArray_avg, '\n',"pop: ", popArray_avg)

#----------Linked list-base Stack----------
class linkedStack:
    #노드 생성 클래스
    class _Node:
        __slots__ = '_element', '_next'

        #노드 초기값
        def __init__(self, element, next):
            self._element = element
            self._next = next

    #스택 초기값
    def __init__(self):
        self._head = None
        self._size = 0
    
    #스택 길이 반환
    def __len__(self):
        return self._size
    
    #스택이 비어있는지 반환
    def isEmpty(self):
        return self._size == 0
    
    #스택에 요소 push
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    #스택에 가장 위에 있는 요소 반환
    def top(self):
        if self.isEmpty():  #스택이 비어있다면 오류 
            raise Empty('Stack is empty')
        return self._head._element

    #스택에 가장 위에 있는 요소 제거 및 반환
    def pop(self):
        if self.isEmpty():  #스택이 비어있다면 오류
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next  #가장 위에 있던 요소의 다음 요소를 첫 번째 요소로 연결
        self._size -= 1  #제거 후 사이즈 축소
        return answer  #가장 위에 있었던 요소 값 반환

    #Stack 출력
    def print_stack(self):
        p = self._head
        while p:
            if p._next != None:  #p가 마지막 요소가 아닐 때
                print(p._element, "-> ", end='')
            else:  #p가 마지막 요소일 때
                print(p._element)
            p = p._next
            
#----------Linked list-base Stack 실행 코드----------
print("\n----Linked list-base Stack----\n")
color = linkedStack()
color.push('red')
color.push('blue')
color.push('yellow')
print("빨강, 파랑, 노랑 push 후:\t", end='')
color.print_stack()
print("top 항목: ", end='')
print(color.top())
color.push('black')
print("검정 push 후:\t", end='')
color.print_stack()
color.pop()
color.push('grey')
print("pop(), 회색 push 후:\t", end='')
color.print_stack()

#----------Linked list-base Stack push & pop time----------
print("\n----Linked list-base Stack push & pop time----\n")

linkedStack = linkedStack()

pushLinked = {}
popLinked = {}
pushLinked_avg = {}
popLinked_avg = {}

k = 10
for j in range(0, 7):
    push_start_time = time.time()
    for i in range(0, k):
        linkedStack.push(i)
    push_end_time = time.time()
    pushTime = push_end_time - push_start_time
    pushLinked[k] = pushTime
    pushLinked_avg[k] = pushTime / k
    
    pop_start_time = time.time()
    for i in range(0, k):
        linkedStack.pop()
    pop_end_time = time.time()
    popTime = pop_end_time - pop_start_time
    popLinked[k] = popTime
    popLinked_avg[k] = popTime / k

    k = k * 10

print("push: ", pushLinked, '\n',"pop: ", popLinked)
print("Average\n push: ", pushLinked_avg, '\n',"pop: ", popLinked_avg)