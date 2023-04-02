class Node: #노드 클래스 정의
    def __init__(self, data): 
        self.data = data
        self.next = None

class linkedQueue: #큐 클래스 정의
    def __init__(self): 
        self.front = None
        self.rear = None

    def isEmpty(self): 
        is_empty = False
        if self.front is None:
            is_empty = True
        return is_empty

    def enqueue(self, data): 
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next

    def dequeue(self):
        deque_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            deque_object = self.front.data
            self.front = self.front.next

        if self.front is None:
            self.rear = None
        return deque_object

    def peek(self):
        front_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            front_object = self.front.data
        return front_object
    
    def display(self, msg):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end=' ')
                node = node.next
            print(node.data, end=' ')
        print()
        

# Driver Code
def testLinkedQueue(): #T(5n+10), O(n)
    print('연결된 구조의 큐 구현\n') #1
    queue = linkedQueue() #1

    for i in range(10): #n
        queue.enqueue(i)
    queue.display('큐 enqueue 9회:') #n
    print('\tdequeue() --> ', queue.dequeue()) #1
    print('\tdequeue() --> ', queue.dequeue()) #1
    print('\tdequeue() --> ', queue.dequeue()) #1

    queue.display('큐 dequeue 3회:') #n
    
    queue.enqueue('수퍼맨') #1
    queue.enqueue('배트맨') #1
    queue.enqueue('원더우먼') #1
    queue.enqueue('아쿠아맨') #1
    
    queue.display('큐 enqueue 4회:') #n
    print('\tdequeue() --> ', queue.dequeue()) #1
    queue.display('큐 dequeue 1회:') #n
    print('\tpeek() --> ', queue.peek()) #1

testLinkedQueue() #Driver Code run