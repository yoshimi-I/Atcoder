# Bowls and Dishes
## 問題
- [Bowls and Dishes](https://atcoder.jp/contests/abc190/tasks/abc190_c)
## 解答
```
N,M = map(int,input().split())
A = list(list(map(int,input().split())) for _ in range(M))
K = int(input())
C = list(list(map(int,input().split())) for _ in range(K))
ans = 0
num = 0
D = [0]*(N+1)

for i in range(2**K):
    for j in range(K):
        if (i >> j) & 1:
            D[C[j][0]] = 1
        else:
            D[C[j][1]] = 1
    for k in range(M):
        if D[A[k][0]] == 1 & D[A[k][1]] ==  1:
            num += 1
    if num >= ans:
        ans = num
    num = 0
    D = [0]*(N+1)
print(ans)
```
## 解説
- 0ならば左の皿にものをのせ、1ならば右の皿に乗せるという処理を行う。
    - つまり試行回数は2**(K人)となる
- そしてその後にM回の試行を行い、どれくらいの数一致しているのかを確認する
- そして全ての処理が終わったらリセット