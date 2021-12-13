#Array-based BST
class BST:
    DEFAULT_CAPACITY = 10000000

    def __init__(self):
        self.tree = [None] * BST.DEFAULT_CAPACITY  #기본 크기가 127이고 None을 원소로 하는 array를 생성

    def put(self, key, value):  #삽입 연산
        i = 0
        self.put_item(i, key, value)

    def put_item(self, index, key, value):
        if self.tree[index] == None:
            self.tree[index] = [key, value]  #삽입
        
        else:
            if key < self.tree[index][0]:  #입력할 key가 현재 key보다 작을 때 
                self.put_item(index*2 + 1, key, value)  #왼쪽 자식에 대해 put_item 실행

            elif key > self.tree[index][0]:  #입력할 key가 현재 key보다 클 때
                self.put_item(index*2 + 2, key, value)  #오른쪽 자식에 대해 put_item실행

            else:
                self.tree[index][1] = value  #이미 key 값이 있을 때 value 수정

    def get(self, key):
        i = 0
        return self.get_item(i, key)
    
    def get_item(self, index, key):
        if self.tree[index] == None:
            return None  #탐색 실패

        if key < self.tree[index][0]:  #찾으려는 키가 현재 키보다 작을 경우
            return self.get_item(index*2 + 1, key)  #왼쪽 subtree 탐색
        
        elif key > self.tree[index][0]:  #찾으려는 키가 현재 키보다 큰 경우
            return self.get_item(index*2 + 2, key)  #오른쪽 subtree 탐색

        else:
            return self.tree[index][1]  #탐색 성공

    def min(self):  #최솟값 인덱스 찾기
        i = 0
        if self.tree[i] == None:
            return None

        return self.minimum(i)

    def minimum(self, index):
        if index*2 + 1 > BST.DEFAULT_CAPACITY:
            return 0
        if self.tree[index*2 + 1] == None:  #왼쪽 child가 없으면 해당 인덱스 리턴
            return index
        
        return self.minimum(index*2 + 1)  #왼쪽 child에 대해 minimum 실행

    def delete_min(self):
        i = self.min()
        self.tree[i] = self.tree[i*2 + 2]

        if self.tree[i*2 + 2] != None:
            self.tree[i*2 + 2] = None

        self.rearrange(i, i*2 + 2)

    def rearrange(self, base, index):
        if index*2 + 1 > BST.DEFAULT_CAPACITY:
            return 0
        if self.tree[index*2 + 1] != None:
            self.tree[base*2 + 1] = self.tree[index*2 + 1]
            self.tree[index*2 + 1] = None
            self.rearrange(base*2 + 1, index*2 + 1)
        
        if self.tree[index*2 + 2] != None:
            self.tree[base*2 + 2] = self.tree[index*2 + 2]
            self.tree[index*2 + 2] = None
            self.rearrange(base*2 + 2, index*2 + 2)

    def delete(self, key):
        i = 0
        self.del_ele(i, key)

    def del_ele(self, index, key):
        if index*2 + 1 > BST.DEFAULT_CAPACITY:
            return 0
        if self.tree[index] == None:
            return None
        
        if key < self.tree[index][0]:
            self.del_ele(index*2 + 1, key)

        elif key > self.tree[index][0]:
            self.del_ele(index*2 + 2, key)

        else:
            if self.tree[index*2 + 1] == None and self.tree[index*2 + 2] == None:
                self.tree[index] = None

            elif self.tree[index*2 + 2] == None:
                self.tree[index] = self.tree[index*2 + 1]
                self.tree[index*2 + 1] = None
                self.rearrange(index, index*2 + 1)

            elif self.tree[index*2 + 1] == None:
                self.tree[index] = self.tree[index*2 + 2]
                self.tree[index*2 + 2] = None
                self.rearrange(index, index*2 + 2)

            else:
                #In-order successor
                i_min = self.minimum(index*2 + 2)
                self.tree[index] = self.tree[i_min]
                self.tree[i_min] = None

                if self.tree[i_min*2 + 2] != None:
                    self.rearrange(i_min, i_min*2 + 2)

    def preorder(self, index):
        if index*2 + 1 > BST.DEFAULT_CAPACITY:
            return 0

        if self.tree[index] != None:
            print(str(self.tree[index][1]), ' ', end='')

            if self.tree[index*2 + 1] != None:
                self.preorder(index*2 + 1)
            
            if self.tree[index*2 + 2] != None:
                self.preorder(index*2 + 2)

    def postorder(self, index):
        if index*2 + 1 > BST.DEFAULT_CAPACITY:
            return 0

        if self.tree[index] != None:
            if self.tree[index*2 + 1] != None:
                self.postorder(index*2 + 1)

            if self.tree[index*2 + 2] != None:
                self.postorder(index*2 + 2)

            print(str(self.tree[index][1]), ' ', end='')

    def inorder(self, index):
        if index*2 + 1 > BST.DEFAULT_CAPACITY:
            return 0

        if self.tree[index] != None:
            if self.tree[index*2 + 1] != None:
                self.inorder(index*2 + 1)

            print(str(self.tree[index][1]), ' ', end='')

            if self.tree[index*2 + 2] != None:
                self.inorder(index*2 + 2)

    def levelorder(self, index):
        l = len(self.tree)
        for i in range(l):
            if self.tree[i] != None:
                print(str(self.tree[i][1]), ' ', end='')

#----------실행 코드----------
b = BST()  #BST 생성
print("-----임의의 10개의 item (key, value) pair 삽입-----")
print("\n(key, value): (1, 5), (4, 7), (10, 0), (2, 5), (8, 10), (3, 5), (5, 9), (6, 1), (9, 4), (7, 7) 삽입")
b.put(1, 5)
b.put(4, 7)
b.put(10, 0)
b.put(2, 5)
b.put(8, 10)
b.put(3, 5)
b.put(5, 9)
b.put(6, 1)
b.put(9, 4)
b.put(7, 7)
print("\n-----임의의 3개 pair 삭제-----")
print("\n(key, value): (3, 5), (6, 1), (8, 10) 삭제")
b.delete(3)
b.delete(6)
b.delete(8)
print("\n-----임의의 2개 key 값에 대한 탐색-----")
print("\nkey: 7, 2 값 탐색")
print("key 7의 value: ", b.get(7))
print("key 2의 value: ", b.get(2))
print("\n-----Traversal 출력-----")
print("\nPre-order")
b.preorder(0)
print("\nPost-order")
b.postorder(0)
print("\nIn-order")
b.inorder(0)
print("\nLevel-order")
b.levelorder(0)

#-----Array-base BST running time analysis-----
import time

b1 = BST()
insertArray = []
deleteArray = []
searchArray = []

print("\n-----Skewed case-----")

k = 5
for j in range(3):
    insert_start_time = time.time()
    for i in range(k):
        b1.put(k-1-i, i + 1)
    insert_end_time = time.time()

    insert_total_time = insert_end_time - insert_start_time
    insert_avg_time = insert_total_time / k

    insertArray.append([k, insert_total_time, insert_avg_time])

    search_start_time = time.time()
    b1.get(k - 1)
    search_end_time = time.time()

    search_time = search_end_time - search_start_time
    searchArray.append([k, search_time])

    delete_start_time = time.time()
    for i in range(k):
        b1.delete_min()
    delete_end_time = time.time()

    delete_total_time = delete_end_time - delete_start_time
    delete_avg_time = delete_total_time / k

    deleteArray.append([k, delete_total_time, delete_avg_time])

    k = k * 2

print("\n", insertArray, "\n")
print("\n", deleteArray, "\n")
print("\n", searchArray, "\n")


print("\n-----Perfect binary case-----")
value = [[3, 1, 5, 0, 2, 4, 6], [15, 7, 23, 3, 11, 19, 27, 1, 5, 9, 13, 17, 21, 25, 29, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
[31, 15, 47, 7, 23, 39, 55, 3, 11, 19, 27, 35, 43, 51, 59, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62]]
insertArrayAvg = []
searchArrayAvg = []
deleteArrayAvg = []
for j in range(len(value)):
    insertAvg_start_time = time.time()
    for i in range(len(value[j])):
        b1.put(value[j][i], value[j][i] + 1)
    insertAvg_end_time = time.time()

    k = len(value[j])
    insertAvg_total_time = insertAvg_end_time - insertAvg_start_time
    insertAvg_avg_time = insertAvg_total_time / k

    insertArrayAvg.append([k, insert_total_time, insert_avg_time])

    searchAvg_start_time = time.time()
    b1.get(k-5)
    searchAvg_end_time = time.time()

    searchAvg_time = searchAvg_end_time - searchAvg_start_time
    searchArrayAvg.append([k, searchAvg_time])

    deleteAvg_start_time = time.time()
    for i in range(k):
        b1.delete_min()
    deleteAvg_end_time = time.time()

    deleteAvg_total_time = deleteAvg_end_time - deleteAvg_start_time
    deleteAvg_avg_time = deleteAvg_total_time / k

    deleteArrayAvg.append([k, deleteAvg_total_time, deleteAvg_avg_time])

print("\n", insertArrayAvg, "\n")
print("\n", deleteArrayAvg, "\n")
print("\n", searchArrayAvg, "\n")