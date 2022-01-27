from random import *

index = 0

for customer in range(1, 51):
    time =  randrange(5, 51)
    
    if 5 <= time <= 15:
        index += 1
        print("[O] {0}번째 손님 소요시간 : {1}분".format(customer, time))
    else:print("[ ] {0}번째 손님 소요시간 : {1}분".format(customer, time))


print("총 탑승 승객 : {0}분".format(index))