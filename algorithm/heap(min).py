import heapq

def solve(A, k):
    n = len(A)
    w = n-k
    while n != w+1:# k번째 수를 만날 때까지
        heapq.heappop(A)
        w += 1
    return A[0]

k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A)
print(solve(A, k))