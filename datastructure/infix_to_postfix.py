#infix-to-postfix 계산기

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val): # O(1)
        self.items.append(val) 
        
    def pop(self): # O(1)
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    
    def top(self): # O(1)
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    
    def __len__(self): # O(1)
        return len(self.items)


opStack = Stack() #stack

outstack = [] #postfix

expr = list("3x2+(5-6)") #infix

def itpfix():
    for token in expr:
        if token not in '+-*/()': 
            outstack.append(token) 

        elif token in '+-*/':
            if token == '*' or token == '/':
                opStack.push(token) 
            elif token == '+' or token == '-':
                    if len(opStack.items) == 0:
                        opStack.push(token)
                    elif len(opStack.items) != 0:
                        while '*' in opStack.items or '/' in opStack.items:
                            outstack.append(opStack.pop())
                            if '(':
                                continue
                    opStack.push(token)

        elif token == '(':
            opStack.push(token)

        elif token == ')':
            while '(' in opStack.items:
                outstack.append(opStack.pop())
                if '(':
                    break
            opStack.items.remove('(')

    while len(opStack) != 0:
        outstack.append(opStack.pop())

itpfix()
print(outstack)