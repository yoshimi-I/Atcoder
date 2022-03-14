# Vacation
## 問題
- [Vacation](https://atcoder.jp/contests/dp/tasks/dp_c)
## 解答
```
N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
check_box = list(list([0]*3) for _ in range(N))
for i in range(N):
    if i == 0:
        check_box[0] = L[0]
    else:
        for j in range(3):
            check_box[i][0] = L[i][0] + max(check_box[i-1][1],check_box[i-1][2])
            check_box[i][1] = L[i][1] + max(check_box[i-1][0],check_box[i-1][2])
            check_box[i][2] = L[i][2] + max(check_box[i-1][0],check_box[i-1][1])
print(max(check_box[N-1]))
```
## 解説
- 今回は3パターンなので全てを羅列してといた。
## 注意点
```
N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
check_box = list(list([0]*3) for _ in range(N))
for i in range(N):
    if i == 0:
        check_box[0] = L[0]
    else:
        for j in range(3):
            check_box[i][0] = check_box[i-1][0] + max(L[i][1],L[i][2])
            check_box[i][1] = check_box[i-1][1] + max(L[i][0],L[i][2])
            check_box[i][2] = check_box[i-1][2] + max(L[i][0],L[i][1])
print(max(check_box[N-1]))
```
- 頭が悪いことに最初このようなコードを書いていた。
- このコードのダメなところはひとつ前と異なった選択肢から選ぶというところを3番目の配列はずっと1,2番目から選ぶという意味合いのコードになってしまっている。
- つまりLのリストが次のリストの最大値を受け取って新しい配列を更新していくコードではダメで、前のリストの最大値を受け取って新しいリストを更新していくようなコードを書かなくてはいけない(デバックすればわかる)