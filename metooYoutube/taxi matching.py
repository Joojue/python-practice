from random import *

index = 0 # 총 입장 팀 수

print("booking list".upper())

for customer in range(1, 16):
    person =  randrange(1, 20)
    
    if 1 <= person <= 8:
        index += 1
        print("[O] {0}번째 예약 팀 : {1}명".format(customer, person))
    else:print("[ ] {0}번째 예약 팀 : {1}명".format(customer, person))


print("총 입장 손님 : {0}팀".format(index))


# 음식점 예약 프로그램
# 사회적 거리두기로 인해 8명 이하의 손님만 입장 가능
# 입장 가능 손님은 옆에 O 표시, 입장 불가한 손님은 공백
# 손님의 숫자는 1부터 20사이의 랜덤한 숫자
# 손님은 총 15팀
