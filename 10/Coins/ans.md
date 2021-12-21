# Coins
## 問題文
- あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
## 入力
- 2
- 2
- 2
- 100
## 出力
- ２
## 解答
```
A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i*500 + j*100 + k*50 == X:
                count += 1
print(count)
```
## 解説
- 普通にネストするだけです(処理速度を考えようね!)
