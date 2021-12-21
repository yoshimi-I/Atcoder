# Placing Marbles
## 問題
- すぬけ君は 1,2,3 の番号がついた 3 つのマスからなるマス目を持っています。 各マスには 0 か 1 が書かれており、マス i には s 
iが書かれています。
すぬけ君は 1 が書かれたマスにビー玉を置きます。 ビー玉が置かれるマスがいくつあるか求めてください。
## 入力例
- 101
## 出力例
- 2

## 解答
```
num = int(input())
x = [a for a in str(num)]
print(x.count("1"))
```
## 解説
numで取り込んだ入力値を一つ一つに分解した後、"1"の数を数え上げた
```
ans = "こんにちは"
test = [i for i in ans]
print(test)
```
- このようにstr型はfor文で1つずつに区切ることができる(str型であることが条件)