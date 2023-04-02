import threading
import time

S = []

def sum1():
    i = 1
    sum1 = 0
    while i <= 200:
        sum1 += i
        i += 1
        time.sleep(0.1)
    print(sum1)
    return S.append(sum1)

def sum2():
    i = 201
    sum2 = 0
    while i <= 400:
        sum2 += i
        i += 1
        time.sleep(0.1)
    print(sum2)
    return S.append(sum2)

def sum3():
    i = 401
    sum3 = 0
    while i <= 600:
        sum3 += i
        i += 1
        time.sleep(0.1)
    print(sum3)
    return S.append(sum3)

def sum4():
    i = 601
    sum4 = 0
    while i <= 800:
        sum4 += i
        i += 1
        time.sleep(0.1)
    print(sum4)
    return S.append(sum4)
def sum5():
    i = 801
    sum5 = 0
    while i <= 1000:
        sum5 += i
        i += 1
        time.sleep(0.1)
    print(sum5)
    return S.append(sum5)

if __name__ == "__main__":
    t1 = threading.Thread(target=sum1)
    t2 = threading.Thread(target=sum2)
    t3 = threading.Thread(target=sum3)
    t4 = threading.Thread(target=sum4)
    t5 = threading.Thread(target=sum5)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print(sum(S))