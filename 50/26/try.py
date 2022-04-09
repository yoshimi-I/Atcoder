from collections import deque
S = deque(input())
swich_num = 1
Q = int(input())
for _ in range(Q):
    L = list(input().split())
    if L[0] == "1":
        swich_num*=(-1)
    if L[0] == "2":
        if L[1] == "1":
            if swich_num > 0:
                S.appendleft(L[2])
            else:
                S.append(L[2])
        else:
            if swich_num > 0:
                S.append(L[2])
            else:
                S.appendleft(L[2])
if swich_num < 0:
    S.reverse()
ans = "".join(S)
print(ans)
