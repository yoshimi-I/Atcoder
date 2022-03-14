from collections import deque
N = int(input())
A = list(map(int,input().split()))
B = deque()
def add_e(a):
    B.append(a)

def add_f(a):
    B.appendleft(a)

for i in range(N):
    if N % 2 == 0:
        if i % 2 != 0:
            add_f(A[i])
        else:
            add_e(A[i])
    else:
        if i % 2 != 0:
            add_e(A[i])
        else:
            add_f(A[i])
print(*B)
