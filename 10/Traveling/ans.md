# Traveling
## 問題
- [Traveling](https://atcoder.jp/contests/abc086/tasks/arc089_a)

## 解答
```
N = int(input())
t = [list(map(int,input().split())) for i in range(N)]
t.insert(0,[0,0,0])
ans = "Yes"
for i in range(1,N+1):
    time_lag = t[i][0] - t[i-1][0]
    position_lag = abs(t[i][1]-t[i-1][1]) + abs(t[i][2]-t[i-1][2])
    if time_lag < position_lag:
        ans = "No"
        break
    if time_lag%2 != position_lag % 2:
        ans = "No"
        break
print(ans)
```
## 解説
- 必ず規則性を見つける
    - イメージは高校数学の数列
- 今回であれば時刻tが1増加するごとにxかyのどちらか1のみ増加、あるいは減少する。
- 今回は2つの条件に該当するしない場合は"NO"を返すプログラムを実行する
    1. ある時間t1からt2の間で移動した距離の合計が(t2-t1)以下である
    2. tが偶数の時はその時の座標の合計も偶数である
    - 以上2点が今回の条件に当たるのでこの条件を満たすのかどうかを考えればいい

## 注意点(間違ったソースコード)
```
N = int(input())
t = [list(map(int,input().split())) for i in range(N)]
t.insert(0,[0,0,0])
ans = "Yes"
for i in range(1,N+1):
    if t[i][0] - t[i-1][0] < abs(t[i][1]-t[i-1][1]) + abs(t[i][2]-t[i-1][2]):
        ans = "No"
        break
    if i%2 != abs(t[i][1] + t[i][2]) % 2:
        ans = "No"
        break
print(ans)
```
- 自分は最初このようなコードを書いていたがこれだと2つ目のif文を調べる回数が1回すくなくなってしまうため不正解
    - イメージとしては1列に並んだ５本の木にそれぞれロープを繋いだ時、ロープは4本でいい(つまり事象-1回数分でいい)
    - このプログラムはfor文の回数がロープの数,2つ目のif文が木の数で1回の違いが出てしまっている