# 解答
```
import math
N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if math.sqrt((L[i][0]-L[j][0])**2 + (L[i][1]-L[j][1])**2) > ans:
                ans = math.sqrt((L[i][0]-L[j][0])**2 + (L[i][1]-L[j][1])**2)
print(ans)
```
# 解説
- 特になし
- impot mathで平方根の計算を可能にした
- あとは全探索