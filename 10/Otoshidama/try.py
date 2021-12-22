N,Y = map(int,input().split())
a = -1
b = -1
c = -1
for i in range(N+1):
    for j in range(N+1-i):
        if 10000*i + 5000*j + 1000*(N-i-j) == Y:
            a = i
            b = j
            c = N-i-j
print(a,b,c)