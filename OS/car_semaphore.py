import random
import threading
import time

sema1 = threading.Semaphore(1)
eve1=threading.Event()
eve2=threading.Event()

def car1():
    for i in range(1, 10):
        car_way = ["직진", "좌회전", "우회전"]
        random.shuffle(car_way)
        print("1방향의 {0}번째 차가 교차로에서 대기중입니다.".format(i))
        eve1.wait()
        eve2.wait()
        sema1.acquire()
        time.sleep(1)
        print("1방향의 {0}번째 차가 {1}으로 교차로를 통과하고 있습니다.".format(i, car_way.pop()))
        print("1방향의 {0}번째 차가 교차로를 통과했습니다.".format(i))
        sema1.release()
        eve1.set()
        eve2.set()

def car2():
    for i in range(1, 10):
        car_way = ["직진", "좌회전", "우회전"]
        random.shuffle(car_way)
        print("2방향의 {0}번째 차가 교차로에서 대기중입니다.".format(i))
        eve2.wait()
        eve1.wait()
        sema1.acquire()
        time.sleep(1)
        print("2방향의 {0}번째 차가 {1}으로 교차로를 통과하고 있습니다.".format(i, car_way.pop()))
        print("2방향의 {0}번째 차가 교차로를 통과했습니다.".format(i))
        sema1.release()
        eve2.set()
        eve1.set()

def car3():
    for i in range(1, 10):
        car_way = ["직진", "좌회전", "우회전"]
        random.shuffle(car_way)
        print("3방향의 {0}번째 차가 교차로에서 대기중입니다.".format(i))
        eve1.wait()
        eve2.wait()
        sema1.acquire()
        time.sleep(1)
        print("3방향의 {0}번째 차가 {1}으로 교차로를 통과하고 있습니다.".format(i, car_way.pop()))
        sema1.release()
        print("3방향의 {0}번째 차가 교차로를 통과했습니다.".format(i))
        eve1.set()
        eve2.set()

def car4():
    for i in range(1, 10):
        car_way = ["직진", "좌회전", "우회전"]
        random.shuffle(car_way)
        print("4방향의 {0}번째 차가 교차로에서 대기중입니다.".format(i))
        eve1.wait()
        eve2.wait()
        sema1.acquire()
        time.sleep(1)
        print("4방향의 {0}번째 차가 {1}으로 교차로를 통과하고 있습니다.".format(i, car_way.pop()))
        sema1.release()
        print("4방향의 {0}번째 차가 교차로를 통과했습니다.".format(i))
        eve1.set()
        eve2.set()

if __name__ == "__main__":
    t1 = threading.Thread(target=car1)
    t2 = threading.Thread(target=car2)
    t3 = threading.Thread(target=car3)
    t4 = threading.Thread(target=car4)
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

print("모든 차량이 교차로를 통과하였습니다.")