N = int(input())
ans_L = dict()
ans = 0
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
if N == 1:
    print(0)
    exit()
L = factorization(N) 
for a,b in L:
    ans_L[a] = b
for j in ans_L:
    for k in range(1,ans_L[j]+1):
        if ans_L[j] >= k:
            ans_L[j] -= k
            ans += 1
        else:
            break
print(ans)