N = int(input())
L = list(map(int,input().split()))
Alice = 0
Bob = 0
list.sort(L, reverse=True)
for i in range(N):
    if i % 2 == 0:
        Alice += L[i]
    else:
        Bob += L[i]
print(Alice-Bob)
