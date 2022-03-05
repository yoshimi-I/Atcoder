#  二分探索の練習問題
## 問題
- [二分探索の練習問題](https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a?lang=ja)
## 解答
```
```
## 解説
- これ正直10^5だから全探索でもREにはならないんですよね笑
- ちなみにその時のソースコードはこちら
```
N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = -1
for i in range(N):
    if K <= A[i]:
        ans = i
        break
print(ans)
```
- というわけでこれを２分探索を用いで実装していこうと思う
```
N,K = map(int,input().split())
A = list(map(int,input().split()))
left_num = 0
right_num = N-1
if K < A[0] or K > A[right_num]:
    print(-1)
    exit()
while (right_num - left_num > 1):
    mid_num = (left_num + right_num)//2
    if A[mid_num] == K:
        print(mid_num)
        exit()
    elif A[mid_num] > K:
        right_num = mid_num
    else:
        left_num = mid_num
print(right_num)
```
- leftとrightを決めてmidを更新していく
- rightとleftが連続したら処理を終わる
```
    if A[mid_num] == K:
        print(mid_num)
        exit()
```
- ここの処理がいらないらしいけど書いた方が簡単なんだよね