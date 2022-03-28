from collections import deque
N = list(input())
ans_0 = deque()
ans_1 = deque()
ans_2 = deque()
mod_sum = 0
for i in N:
    i = int(i)
    mod = i%3
    if mod==0:
        ans_0.appendleft(i)
    elif mod==1:
        ans_1.appendleft(i)
    else:
        ans_2.appendleft(i)
    mod_sum += mod
    mod_sum = mod_sum%3

if mod_sum == 0:
    print(0)
    exit()
elif mod_sum == 1:
    if len(ans_1) >= 1:
        ans_1.popleft()
        if len(ans_0) ==0 and len(ans_1) ==0 and len(ans_2) ==0:
            print(-1)
            exit()
        else:
            print(1)
            exit()
    elif len(ans_2) >= 2:
        ans_2.popleft()
        ans_2.popleft()
        if len(ans_0) ==0 and len(ans_1) ==0 and len(ans_2) ==0:
            print(-1)
            exit()
        else:
            print(2)
            exit()
    else:
        print(-1)
        exit()
else:
    if len(ans_2) >= 1:
        ans_2.pop()
        if len(ans_0) ==0 and len(ans_1) ==0 and len(ans_2) ==0:
            print(-1)
            exit()
        else:
            print(1)
            exit()
    elif len(ans_1) >= 2:
        ans_1.pop()
        ans_1.pop()

        if len(ans_0) ==0 and len(ans_1) ==0 and len(ans_2) ==0:
            print(-1)
            exit()
        else:
            print(2)
            exit()
    else:
        print(-1)

