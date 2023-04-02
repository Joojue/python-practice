class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def preorder(self,n):
        if n != None:
            print(n.item,' ',end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
    
    def inorder(self, n):
        if n != None:
            if n.left:
                self.preorder(n.left)
            print(n.item,' ',end='')
            if n.right:
                self.preorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
            print(n.item,' ',end='')
    
    def levelorder(self, root):
        q=[]
        q.append(root)
        while q:
            t=q.pop(0)
            print(t.item,' ',end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def getCount(self, n):
        count = 0
        if n != None:
            count = 1 + self.getCount(n.left) + self.getCount(n.right)
        return count

    def leafCount(self, n):
        count = 0
        if n != None:
            if n.left == None and n.right == None:
                return 1
            else:
                count = self.leafCount(n.left) + self.leafCount(n.right)
        return count


tree = BinaryTree()
n1 = Node("+")
n2 = Node("*")
n3 = Node("E")
n4 = Node("*")
n5 = Node("D")
n6 = Node("/")
n7 = Node("C")
n8 = Node("A")
n9 = Node("B")

tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right= n5
n4.left = n6
n4.right = n7
n6.left = n8
n6.right = n9

print('트리 높이 : ', tree.height(tree.root))

print('노드 개수 : ', tree.getCount(tree.root))

print('단말 노드 개수 : ', tree.leafCount(tree.root))

print('전위 순회 : ', end='')
tree.preorder(tree.root)

print('\n중위 순회 : ', end='')
tree.inorder(tree.root)

print('\n후위 순회 : ', end='')
tree.postorder(tree.root)

print('\n레벨 순회 : ', end='')
tree.levelorder(tree.root)