# 問題
- [Rotate](https://atcoder.jp/contests/abc235/tasks/abc235_a)
## 自分の解答
```
num = input()
num = str(num)
list_num = list(num)
list_num = [int(s) for s in list_num]
a = int(list_num[0])
b = int(list_num[1])
c = int(list_num[2])
a1 = a*100 + b*10 +c
a2 = b*100 + c*10 + a
a3 = c*100 + a*10 + b
print(a1+a2+a3)  
```
## 模範解答
```
num = input()
a = int(num[0])
b = int(num[1])
c = int(num[2])
print(111*(a + b + c )
```
## 反省点
- 頭が悪すぎた
- スマートに解きたい物である