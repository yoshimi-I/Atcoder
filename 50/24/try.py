N,M,X = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(N))
ans = 10000000000
for i in range(2**N):
    ans_l = [0 for _ in range(M)]
    suu_num = 0
    for j in range(N):
        if (i>>j) &1:
            for k in range(1,M+1):
                ans_l[k-1] += L[j][k]
            suu_num += L[j][0]
    if min(ans_l) >= X:
        if ans > suu_num:
            ans = suu_num
if ans == 10000000000:
    print(-1)
else:
    print(ans)
