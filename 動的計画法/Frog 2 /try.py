N, K = map(int,input().split())
h = list(map(int,input().split()))
table = [0]*N
for i in range(1,N):
    if i == 1:
        table[1] = abs(h[1]-h[0])
    else:
        a = 10000000000
        for j in range(1,K+1):    
            if i -j <0:
                continue
            b = table[i-j] + abs(h[i] -h[i-j])
            if b <= a:
                a = b
        table[i] = a
print(table[N-1])