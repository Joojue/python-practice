import random, timeit

def quick_sort(A, first, last):
    global Qc, Qs
    if first >= last: return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
            Qc += 1
        while right > first and A[right] >= pivot:
            right -= 1
            Qc += 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            Qs += 1
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)

def quick_sort_i(A, first, last):
    global Qic, Qis
    if last-first <= 10:
        insertion_sort_q(A[first:last+1])
        return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
            Qic += 1
        while right > first and A[right] >= pivot:
            right -= 1
            Qic += 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            Qis += 1
    A[first], A[right] = A[right], A[first]
    Qis += 1
    quick_sort_i(A, first, right-1)
    quick_sort_i(A, right+1, last)

def merge_sort(A, first, last):
    global Mc, Ms
    if first >= last: return
    middle = (first+last)//2
    merge_sort(A, first, middle)
    merge_sort(A, middle+1, last)
    B = []
    i = first
    j = middle+1
    while i <= middle and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
            Mc += 1
            Ms += 1
        else:
            B.append(A[j])
            j += 1
            Mc += 1
            Ms += 1

    for i in range(i, middle+1):
        B.append(A[i])
        Ms += 1
    for j in range(j, last+1):
        B.append(A[j])
        Ms += 1
    for k in range(first, last+1):
        A[k] = B[k-first]
        Ms += 1

def merge_sort_i(A, first, last):
    global Mic, Mis
    if last-first <= 10:
        insertion_sort_m(A[first:last+1])
        return
    middle = (first+last)//2
    merge_sort_i(A, first, middle)
    merge_sort_i(A, middle+1, last)
    B = []
    i = first
    j = middle+1
    while i <= middle and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
            Mic += 1
            Mis += 1
        else:
            B.append(A[j])
            j += 1
            Mic += 1
            Mis += 1

    for i in range(i, middle+1):
        B.append(A[i])
        Mis += 1
    for j in range(j, last+1):
        B.append(A[j])
        Mis += 1
    for k in range(first, last+1):
        A[k] = B[k-first]
        Mis += 1

def make_heap(A):
    n = len(A)
    for k in range(n-1, -1, -1):
        heapify_down(A, k, n)

def heapify_down(A, k, n):
    global Hc, Hs
    while 2*k+1 < n:
        L, R = 2*k+1, 2*k+2
        if L < n and A[L] > A[k]:
            m = L
            Hc += 1 
        else:
            m = k
        if R < n and A[R] > A[m]:
            m = R
            Hc += 1
        if m != k:
            A[k], A[m] = A[m], A[k]
            k = m
            Hs += 1
        else: break

def heap_sort(A):
    global Hs
    make_heap(A)
    n = len(A)
    for k in range(n-1, -1, -1):
        A[0], A[k] = A[k], A[0]
        Hs += 1
        n = n-1
        heapify_down(A, 0, n)

def insertion_sort_q(A):
    global Qic, Qis
    for a in range(1, len(A)):
        for b in range(a, 0, -1):
            Qic += 1
            if A[b] < A[b-1]:
                A[b], A[b-1] = A[b-1], A[b]
                Qis += 1
            else:
                break
    return A

def insertion_sort_m(A):
    global Mic, Mis
    for a in range(1, len(A)):
        for b in range(a, 0, -1):
            Mic += 1
            if A[b] < A[b-1]:
                A[b], A[b-1] = A[b-1], A[b]
                Mis += 1
            else:
                break
    return A
                
        


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs, Qic, Qis, Mic, Mis = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))
print("Quick sort_i:")
print("time =", timeit.timeit("quick_sort_i(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qic, Qis))
print("Merge sort_i:")
print("time =", timeit.timeit("merge_sort_i(E, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mic, Mis))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))