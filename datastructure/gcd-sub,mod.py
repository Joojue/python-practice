# 최대공약수(gcd)구하기 - sub

def gcd(a,b):
    while a != 0 and b != 0:
        if a > b: a = a-b
        else: b = b-a
    return print(a+b)
gcd(78652, 86002)

# 최대공약수(gcd)구하기 - mod

def gcd(a,b):
    if a > b: print(int(a/b))
    else: print(int(b/a))
gcd(16,6)