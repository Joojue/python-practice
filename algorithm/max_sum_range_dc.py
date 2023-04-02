def max_sum(A, left, right):
    if left == right: return A[left]

    m = (left+right)//2
    L1 = max_sum(A, left, m)
    R1 = max_sum(A, m+1, right)

    w = 0
    L2 = min(A)
    for i in range(m, left-1, -1):
        w += A[i]
        L2 = max(L2, w)

    w = 0
    R2 = min(A)
    for i in range(m+1, right+1):
        w += A[i]
        R2 = max(R2, w)

    return max(L1, R1, L2+R2)


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)