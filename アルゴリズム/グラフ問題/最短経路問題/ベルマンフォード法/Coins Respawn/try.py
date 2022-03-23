N,M,P = map(int,input().split())
path = []
for _ in range(M):
    A,B,C = map(int,input().split())
    path.append([A,B,C])
coin_check = [-10000000000000]*(N+1)
check_ans = 0
coin_check[1] = 0
for i in range(2*N):
    check_num = 0
    for now,next,coin in path:
        if coin_check[next] < coin_check[now] + coin - P:
            if coin_check[now] >= 0 and coin_check[now] + coin - 10 < 0:
                coin_check[next] = 0
            else:
                coin_check[next] = coin_check[now] + coin - P
    if i == N-2:
        check_ans = coin_check[N]
if check_ans != coin_check[N]:
    print(-1)
else:
    print(coin_check[N])

