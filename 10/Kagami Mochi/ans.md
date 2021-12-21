# Kagami Mochi
## 問題
- [Kagami Mochi](https://atcoder.jp/contests/abc085/tasks/abc085_b)
## 解答
```
N = int(input())
d = list(int(input()) for i in range(N))
print(len(set(d)))
```
## 解説
- set関数を用いる
    - set関数とは配列の中から重複するものを取り出してくれる