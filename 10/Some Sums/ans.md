# Some Sums
## 問題文
- [Some Sums](https://atcoder.jp/contests/abc083/tasks/abc083_b)
## 解答
```
N,A,B = map(int,input().split())
sum = 0
def sum_num(num):
    first = 0
    while num >0:
        first += num%10
        num = num//10
    return(first)
    
for i in range(N+1):
    if sum_num(i) >= A and sum_num(i) <= B:
        sum += i
print(sum)
```
## 解説
- 各々のくらいの数を足すには10で割っていけばいい、そしれ商が0になったときwhile文を抜けるようにすればいい。
- それを関数にしたあたfor文の中にぶち込んで足し合わせていく