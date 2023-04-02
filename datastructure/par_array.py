# 괄호 맞추기

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

S = Stack()

parseq = list("(())()()((()))()()(")

def par_array():
    for p in parseq:
        if p =='(' : S.push(p)
        elif len(S) != 0 and p == ')' : S.pop()
        elif len(S) == 0 and p == ')' : return False
        else : print("Not allowed Symbol")

    if len(S) > 0 : return False

    else : return True

a = par_array()

if a == True :
    print("괄호가 맞습니다")
else : print("괄호가 맞지 않습니다")

par_array()