from random import *
users = range(1, 21)
users = list(users)
shuffle(users)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :", users.pop())
print("커피 당첨자 :", sample(users, 3))
print("-- 축하합니다 --")