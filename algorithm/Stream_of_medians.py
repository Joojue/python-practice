import time

def Stream_of_medians(A):
    median = []
    for k in range(0, len(A)):
        B = sorted(A[:k+1])
        median.append(B[((k)//2)])
    return sum(median)


A = [int(x) for x in input().split()]
print(Stream_of_medians(A))