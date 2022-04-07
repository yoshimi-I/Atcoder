N,K= map(int,input().split())
p = list(map(int,input().split()))
ans = 0
def kitaichi(num):
    add = num
    count = 0
    while add > 0:
        count += add
        add -= 1
    return float(count)/float(num)
L = []
for i in range(N):
    if i == 0:
        L.append(kitaichi(p[i]))
    else:
        L.append(kitaichi(p[i]) + L[i-1])
for j in range(K-1,N):
    if j == K-1:
        check = L[j]
    else:
        check = L[j]-L[j-K]
    if check >= ans:
        ans = check
print(ans)
