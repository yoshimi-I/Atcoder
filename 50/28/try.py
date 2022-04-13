H,W,K=map(int, input().split())
C = list(list(input()) for _ in range(H))
ans=0
for y in range(2**H):
    for x in range(2**W):
        black_num = 0
        for i in range(H):
            for j in range(W):
                if ((y>>i)&1 == False) and ((x>>j)&1 == False):
                    if C[i][j] == "#":
                        black_num +=1
        if black_num == K:
            ans += 1
print(ans)


