def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if (A[j] < A[least]):
                least = j
        A[i], A[least] = A[least], A[i]

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChange = False
        for j in range(i):
            if (A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j] # 교환
                bChange = True # 교환 발생
        if not bChange: break # 교환이 없으면 종료

def __eq__(self, setB):
    if self.size() != setB.size() :
        return False
    for idx in range(len(self.items)):
        if self.items[idx] != setB.items[idx]:
            return False
    return True

def union(self, setB):
    newSet = Set()
    a = 0
    b = 0
    while a < len(self.items) and b < len(setB.tems):
        valueA = self.items[a]
        valueB = setB.items[b]
        if valueA < valueB:
            newSet.items.append(valueA)
            a += 1
        elif valueA > valueB:
            newSet.items.append(valueB)
            b += 1
        else:
            newSet.items.append(valueA)
            a += 1
            b += 1
    while a < len(self.items):
        newSet.items.append(self.items[a])
        a += 1
    while b < len(setB.items):
        newSet.items.append(setB.items[b])
        b += 1
    return newSet

def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i].key == key:
            return i
    return None

def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle].key:
            return middle
        elif (key < A[middle].key):
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return None

def binary_search_iter(A, key, low, high):
    while(low <= high):
        middle = (low + high) // 2
        if key == A[middle].key:
            return middle
        elif (key > A[middle].key):
            low = middle + 1
        else:
            high = middle - 1
    return None

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
        
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    queue = CircularQueue() # 큐 객체 초기화
    queue.enqueue(root) # 최초에 큐에는 루트 노드만 들어있음
    while not queue.isEmpty(): # 큐가 공백 상태가 아닌 동안,
        n = queue.dequeue() # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None: 
            print(n.data, end=' ') # 노드의 정보 출력
            queue.enqueue(n.left) # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right) # n의 오른쪽 자식 노드를 큐에 삽입

def count_node(n):
    if n is None:
        return 0
    else:
        return 1+ count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1

class MaxHeap:
    def __init__(self):
        self.heap=[]
        self.heap.append(0)

    def size(self): return len(self.heap) -1
    def isEmpty(self): return self.sze() == 0
    def Parent(self, i): return self.heap[i//2]
    def Left(self, i): return self.heap[i*2]
    def Right(self, i): return self.heap[i*2+1]
    def display(self, msg = '힙 트리: '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n > self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

def delete(self):
    parent = 1
    child = 2
    if not self.isEmpty():
        hroot = self.heap[1] # 삭제할 루트 복사
        last = self.heap[self.size()] # 마지막 노드
        while (child <= self.size()): # 마지막 노드 이전까지
            # 만약 오른쪽 노드가 더 크면 child를 1증가 (기본은 왼쪽 노드)
            if child < self.size() and self.Left(parent) < self.Right(parent):
                child += 1
            if last >= self.heap[child]: # 더 큰 자식이 더 작으면
                break # 삽입 위치 발견. 종료
            self.heap[parent] = self.heap[child] # 아니라면 계속 진행
            parent = child
            child *= 2
        
        self.heap[parent] = last # 맨 마지막 노드를 parent 위치에 복사
        self.heap.pop(-1) # 맨 마지막 노드 삭제
        return hroot # 저장해두었던 루트 반환

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key > n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_value_bst(n, value):
    if n == None : return None
    elif value == n.value: # n의 value와 동일 > 탐색 성공
        return n 
    res = search_value_bst(n.left, value) # 왼쪽서브트리 탐색
    if res is not None: # 성공이면 반환
        return res
    else: # 실패면 오른쪽에서 반환
        return search_value_bst(n.right, value)

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return None
        else:
            return insert_bst(r.right, n)
    else:
        return False

def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    return root

def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child

    return root

def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while (succ.left != None):
        succp = succ
        succ = succ.left

    if (succp.left == succ):
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value

    return root

def delete_bst (root, key):
    if root == None: return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else: node = node.right

    if node == None: return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)
    return root

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def reBalance (parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
        
    return parent

def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")

