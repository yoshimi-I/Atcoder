from typing import Counter


N,L = map(int,input().split())
K = int(input())
A = [0]+ list(map(int,input().split()))
A.append(L)

def ans(x):
    count = 0
    l = 0
    for i in range(N+1):
        l += A[i+1] - A[i]
        if l >= x:
            count += 1
            l = 0
    if count >= K+1:
        return(True)
    else:
        return(False)
left = 0
right = L
while right - left > 1:
    mid = (left + right)//2
    if ans(mid):
        left = mid
    else:
        right = mid
print(left)
