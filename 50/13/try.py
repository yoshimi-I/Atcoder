N,X = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(N))
count = 0
alc = 0
for i,j in L:
    alc += i*j
    count += 1
    if alc > X*100:
        print(count)
        exit()
print(-1)
