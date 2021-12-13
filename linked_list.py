#Linked list

#Single linked list
class SList:
    #노드를 생성하는 클래스 노드는 아이템과 다음 노드 래퍼런스를 가진다.
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link
        
    #초기 linked list 생성 요소가 없기 때문에 head는 none을 가리키고 size는 0이다.
    def __init__(self):
        self.head = None
        self.size = 0
    
    #linked list의 크기를 리턴
    def size(self):
        return self.size
    
    #linked list가 비어있는지 리턴
    def isEmpty(self):
        return self.size == 0

    #linked list의 가장 앞에 새 노드 삽입
    def add_front(self, item):
        if self.isEmpty():  #linked list가 비어있을 때
            self.head = self.Node(item, None)  #노드를 생성하여 head가 가리키게 하고 새 노드는 None을 가리키게 한다.
        else:
            self.head = self.Node(item, self.head)  #노드를 생성하여 head가 가리키게 하고 생성된 노드는 기존의 첫 번째 요소를 가리키게 한다.
        self.size += 1  #새 노드르 삽입하였기 때문에 사이즈를 1 늘린다.

    #linked list에서 p가 가리키는 노드 다음에 새 노드 삽입
    def add_after(self, item, p):
        p.next = self.Node(item, p.next)  #새 노드를 생성하여 p가 가리키는 노드로 지정하고 새 노드는 기존 p가 가리키던 노드를 가리키도록 한다.
        self.size += 1

    #linked list에서 가장 앞의 노드 삭제
    def del_front(self):
        if self.isEmpty():  #list가 비어있다면 에러 발생
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next  #첫 번째 노드가 가리키는 노드를 첫 번째 노드로 지정한다.
            self.size -= 1  #노드를 삭제하였기 때문에 사이즈를 1 줄인다.

    #linked list에서 p가 가리키는 가음 요소 삭제
    def del_after(self, p):
        if self.isEmpty():  #list가 비어있다면 에러 발생
            raise EmptyError('Underflow')
        else:
            t = p.next  #t를 p가 가리키는 노드로 지정
            p.next = t.next  #p가 가리키는 노드를 t가 가리키는 노드로 지정
            self.size -= 1  #삭제하였기 때문에 사이즈를 1 줄인다.

    #노드 탐색
    def search(self, target):
        p = self.head  #첫 번째 노드부터 순차적으로 탐색
        for i in range(self.size):
            if target == p.item:
                return i  #탐색 성공
            p = p.next
        return None  #탐색 실패

    #linked list 출력
    def print_list(self):
        p = self.head
        while p:
            if p.next != None:  #p가 마지막 요소가 아닐 때
                print(p.item, "-> ", end='')
            else:  #p가 마지막 요소일 때
                print(p.item)
            p = p.next

    #에러 처리
    class EmptyError(Exception):
        pass

#Double linked list
class DList:
    #노드를 생성하는 클래스 노드는 아이템과 이전, 다음 노드 래퍼런스를 가진다.
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    #초기값
    def __init__(self):
        self.head = self.Node(None, None, None)  #head 노드 tail 노드를 생성하기 전이기 때문에 다음 노드는 None으로 한다.
        self.tail = self.Node(None, self.head, None)  #tail 노드 이전 노드를 head 노드로 지정
        self.head.next = self.tail  #head 노드가 다음으로 가리키는 노드를 tail 노드로 지정
        self.size = 0  #item이 없는 상태이기 때문에 크기는 0

    #크기를 반환
    def size(self):
        return self.size
    
    #리스트가 비어있는지 반환
    def isEmpty(self):
        return self.size == 0

    #p 앞에 새 노드 삽입
    def add_before(self, p, item):
        t = p.prev  #p의 이전 노드를 t로 지정
        n = self.Node(item, t, p)  #새로운 노드 생성 이전 노드는 t로 다음 노드는 p로 지정하고 이를 n으로 지정
        p.prev = n  #n을 p의 이전 노드로 지정
        t.next = n  #n을 t의 다음 노드로 지정
        self.size += 1  #삽입을 하였으므로 크기를 1 늘린다.

    #p 다음에 새 노드 삽입
    def add_after(self, p, item):
        t = p.next  #p의 다음 노드를 t로 지정
        n = self.Node(item, p, t)  #새로운 노드 생성 이전 노드는 p로 다음 노도는 t로 지정하고 이를 n으로 지정
        t.prev = n  #n을 t의 이전 노드로 지정
        p.next = n  #n을 p의 다음 노드로 지정
        self.size += 1  #삽입을 하였으므로 크기를 1 늘린다.

    #x에 있는 노드 삭제
    def delete(self, x):
        f = x.prev  #x의 이전 노드를 f로 지정
        r = x.next  #x의 다음 노드를 r로 지정
        f.next = r  #r을 f의 다음 노드로 지정
        r.prev = f  #f를 r의 이전 노드로 지정
        self.size -= 1  #삭제를 하였으므로 크기를 1 줄인다.
        return x.item  #삭제한 노드의 값을 반환
    
    #리스트를 출력
    def print_list(self):
        if self.isEmpty():  #빈 리스트라면 비어있다고 출력
            print("List is empty")
        else:
            p = self.head.next  #첫 번째 노드를 p로 지정
            while p != self.tail:  #p가 tail 노드가 아니면 실행
                if p.next != self.tail:  #p의 다음 노드가 tail 노드가 아니면 다음을 출력
                    print(p.item, '<=> ', end='')
                else:
                    print(p.item)
                p = p.next


#Single linked list 실행 코드
print("\n----Single linked list----\n")
s = SList()
s.add_front('orange')
s.add_front('apple')
s.add_after('cherry', s.head.next)
s.add_front('pear')
s.print_list()

print('cherry는 %d번째' % (s.search('cherry') + 1))
print('kiwi는', s.search('kiwi'))

print('배 다음 노드 삭제 후:\t\t', end='')
s.del_after(s.head)
s.print_list()

print("첫 노드 삭제 후:\t\t", end='')
s.del_front()
s.print_list()

print('첫 노드로 망고, 딸기 삽입 후:\t', end='')
s.add_front('mango')
s.add_front('strawberry')
s.print_list()

print('오렌지 다음 노드 삭제 후:\t', end='')
s.del_after(s.head.next.next)
s.print_list()

#Double linked list 실행 코드
print("\n----Double linked list----\n")
d = DList()
d.add_after(d.head, 'apple')
d.add_before(d.tail, 'orange')
d.add_before(d.tail, 'cherry')
d.add_after(d.head.next, 'pear')
d.print_list()

print("마지막 노드 삭제 후:\t", end='')
d.delete(d.tail.prev)
d.print_list()

print("맨 끝에 포도 삽입 후:\t",  end='')
d.add_before(d.tail, 'grape')
d.print_list()

print("첫 노드 삭제 후:\t", end='')
d.delete(d.head.next)
d.print_list()

print("첫 노드 삭제 후:\t", end='')
d.delete(d.head.next)
d.print_list()

print("첫 노드 삭제 후:\t", end='')
d.delete(d.head.next)
d.print_list()

print("첫 노드 삭제 후:\t", end='')
d.delete(d.head.next)
d.print_list()