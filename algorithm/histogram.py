B, n = map(int, input().split())
F=[0]*n
for i in range(0, n):
    F[i] = int(input())

def Histogram():
    global B
    for i in range(1, B):
        inp = F[i-1]
        globals()["pivot_{}".format(i)] = inp

Histogram()
print(pivot_1, pivot_2)
    # if left == right: return B[left]

    # m = (left+right)//2
    # L1 = Histogram(B, left, m)
    # R1 = Histogram(B, m+1, right)

    # w = 0
    # L2 = min(B)
    # for i in range(m, left-1, -1):
    #     w += B[i]
    #     L2 = max(L2, w)

    # w = 0
    # R2 = min(B)
    # for i in range(m+1, right+1):
    #     w += B[i]
    #     R2 = max(R2, w)

    # return max(L1, R1, L2+R2)

# 우선 리스트 F를 B개로 분할