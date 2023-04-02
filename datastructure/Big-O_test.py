def algorithm_ArrayMax():
    A = [2, -1, 3, 12, 6]
    currentMax = A[0]
    for i in range(0, len(A)):
        if currentMax <= A[i]:
            currentMax = A[i]
    return currentMax
# T(n) = 2n-1 O(n)

def algorithm_sum1():
    sum = 0
    A = [2, 4, 6, 7, 8, 9, 11, 14, 15, 17, 18]
    for i in range(0, len(A)):
        if A[i]%2 == 0:
            sum += A[i]
    return sum
# T(n) = 4n+1 O(n)

def algorithm_sum2():
    sum = 0
    A = [2, 4, 6]
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            sum += A[i]*A[j]
    return sum
# T(n) = 3/2n^2 - 3/2n +1 O(n^2)


def numberof_bits(n):
    count = 0
    while n > 1:
        n = n//2
        count += 1
    return count
# T(n) 4log(2,n) +1 = 0 O(logn)