A = list(input())

def two_max(A,left,right):
    if right-left==1:
        if A[right]>A[left]:
            M,m=A[right],A[left]
        else:
            M,m=A[left],A[right]
        return M,m
    if left==right:
        return A[left],None
	
    mid=(left+right)//2
    M1,m1=two_max(A,left,mid)
    M2,m2=two_max(A,mid+1,right)

    if M1>M2 and mid >= 1:
        if (m1!=None and M2>m1):
            M,m=M1,M2
        else:
            M,m=M1,m1
    else:
        if (m2!=None and M1>m2):
            M,m=M2,M1
        else:
            M,m=M2,m2
    return M,m

M, m = two_max(A, 0, len(A)-1)
print(M, m)