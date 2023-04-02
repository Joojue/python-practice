import time, random

X = []

def prefixSum1(X, n):
    while len(X) != n:
        X.append(random.randint(-999, 999))
    S = [0]*n
    for i in range(0, n):
        for j in range(0, i+1):
            S[i] += X[j]
    return S


def prefixSum2(X, n):
    while len(X) != n:
        X.append(random.randint(-999, 999))
    S = [0]*n
    S[0] = X[0]
    for i in range(1, n):
        S[i] = S[i-1] + X[i]
    return S


random.seed()

before = time.process_time()
prefixSum1(X, n)
after = time.process_time()
print(after - before)

before = time.process_time()
prefixSum2(X, n)
after = time.process_time()
print(after - before)