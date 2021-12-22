# Otoshidama
## 問題
- [Otoshidama](https://atcoder.jp/contests/abc085/tasks/abc085_c)

## 解答
```
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
```
## 解説
- 特にこれといった知識は使わなかった
- a,b,cをそれぞれのお札の枚数とするとcはaとbから導き出せるため実質変数はa,bの２つで良くなる。という当たり前のことをコードに落とし込む