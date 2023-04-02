def fibo(n):
    i = 2
    a = 1
    b = 0
    if n == 0:
        print(1)
    while (True):
        if n + 1 == i:
            print((a+b))
        i += 1
        a,b = a+b,a

fibo(7)