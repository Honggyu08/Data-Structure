class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left

class BST:
    def __init__(self):  #트리 생성
        self.root = None

    def get(self, key):  #탐색 연산
        return self.get_item(self.root, key)
    
    def get_item(self, n, k):
        if n == None:  #탐색 실패
            return None
        
        if n.key > k:  #k가 노드의 key보다 작으면 왼쪽 subtree 탐색
            return self.get_item(n.left, k)
        
        elif n.key < k:  #k가 노드의 key보다 크면 오른쪽 subtree 탐색
            return self.get_item(n.right, k)
        
        else:
            return n.value  #탐색 성공

    def put(self, key, value):  #삽입 연산
        self.root = self.put_item(self.root, key, value)  #root와 put_item이 리턴하는 노드를 연결
    
    def put_item(self, n , key, value):
        if n == None:
            return Node(key, value)  #새 노드 생성
        
        if n.key > key:  #입력할 노드의 키 값이 현재 노드의 키 값보다 작을 때
            n.left = self.put_item(n.left, key, value)  #왼쪽 자식과 put_item이 리턴하는 노드를 연결
        
        elif n.key < key:  #입력할 노드의 키 값이 현재 노드의 키 값보다 클 때
            n.right = self.put_item(n.right, key, value)  #오른쪽 자식과 put_item이 리턴하는 노드를 연결
        
        else:  #키 값이 이미 있을 때
            n.value = value  #value 수정
        
        return n  #현재 노드를 리턴

    def min(self):  #최솟값 가진 노드 찾기
        if self.root == None:  #root가 없다면
            return None  #None을 리턴
        
        return self.minimun(self.root) 

    def minimun(self, n):  #재귀호출하여 최솟값을 찾아 리턴하는 함수
        if n.left == None:  #왼쪽 자식이 없다면 해당 노드를 리턴
            return n

        return self.minimun(n.left)  #재귀호출

    def delete_min(self):  #최솟값 삭제
        if self.root == None:  #root가 없다면
            print("트리가 비어있음")

        self.root = self.del_min(self.root)  #del_min이 리턴하는 노드를 root로 연결

    def del_min(self, n):
        if n.left == None:
            return n.right  #왼쪽 자식이 없다면 오른쪽 자식 리턴
        
        n.left = self.del_min(n.left)  #왼쪽 자식의 del_min이 리턴하는 값을 왼쪽 자식으로 연결
        return n  #해당 노드 리턴

    def delete(self, k):  #삭제 연산
        self.root = self.del_node(self.root, k)  #del_node가 리턴하는 노드를 root에 연결

    def del_node(self, n, k):
        if n == None:
            return None
        
        if n.key > k:
            n.left = self.del_node(n.left, k)

        elif n.key < k:
            n.right = self.del_node(n.right, k)
        
        else:
            if n.right == None:
                return n.left
            
            if n.left == None:
                return n.right
            
            #In-order successor
            target = n
            n = self.minimun(target.right)  #오른쪽 subtree 중 가장 작은 값을 n노드와 연결
            n.right = self.del_min(target.right)  #n의 오른쪽 자식을 n을 제거한 target의 오른쪽 subtree로 연결
            n.left = target.left  #왼쪽 subtree는 변하지 않음
        
        return n

    def preorder(self, n):  #CLR
        if n != None:
            print(str(n.value), ' ', end='')  #CLR이므로 root 먼저 출력
            if n.left:
                self.preorder(n.left)  #left child가 있을 경우 left child에대해 preoder실행
            if n.right:
                self.preorder(n.right)  #right child가 있을 경우 right child에대해 preoder실행

    def postorder(self, n):  #LRC
        if n != None:
            if n.left:
                self.postorder(n.left)  #left child가 있을 경우 left child에대해 postoder실행
            if n.right:
                self.postorder(n.right)  #right child가 있을 경우 right child에대해 postoder실행

            print(str(n.value), ' ', end='')  #left child, right child에 대해 실행한 후 root를 가장 마지막에 출력

    def inorder(self, n):  #LCR
        if n != None:
            if n.left:
                self.inorder(n.left)  #left child가 있을 경우 left child에대해 inoder실행
            
            print(str(n.value), ' ', end='')  #left child에대해 실행이 끝나면 root 출력

            if n.right:
                self.inorder(n.right)  #right child가 있을 경우 right child에대해 inoder실행

    def levelorder(self, root):
        q = []  #각 level의 노드를 입력 받고 출력으로 보내기 위해 큐 생성
        q.append(root)  #큐에 root 입력

        while len(q) != 0:  #큐가 빌 때까지 실행
            t = q.pop(0)
            print(str(t.value), ' ', end='')
            #dequeue를 통해 출력

            if t.left != None:
                q.append(t.left)
            
            if t.right != None:
                q.append(t.right)
            #현재 노드의 자식들 큐에 순서대로 입력

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
b.preorder(b.root)
print("\nPost-order")
b.postorder(b.root)
print("\nIn-order")
b.inorder(b.root)
print("\nLevel-order")
b.levelorder(b.root)

#-----link-base BST running time analysis-----
import time

b1 = BST()
insertArray = []
deleteArray = []
searchArray = []

print("\n-----Skewed case-----")

k = 100
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