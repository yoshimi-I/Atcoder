# Frog 2 
## 問題
- [Frog 2 ](https://atcoder.jp/contests/dp/tasks/dp_b)
## 解答
```
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
```
## 解説
- やっていることはFrog1の応用です。
- for j in range(1,K+1):  でそれぞれKの数ぶん前に戻って最小値を求めていきます。
- しかし問題はjのループの方が早いのでi -j <0の時が生まれてしまう。
    - そんな時にcontinueすることでスキップしている