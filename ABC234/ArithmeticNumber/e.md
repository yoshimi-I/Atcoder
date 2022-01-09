# 解答
```
N = input()
if len(N) <= 2:
    print(int(N))
    exit()
if len(N) >= 11:
    if int(N[0]) == 9:
        print(int(str(9)*(len(N))))
    elif int(N)-int(str(int(N[0]))*(len(N)))>0:
        print(int(str(int(N[0])+1)*(len(N))))
 
    else:
        print(int(str(int(N[0]))*(len(N))))
    exit()
N = int(N)
ans_a = 1
 
for k in range(1,10):
    ans_a = k
    for i in range(-9,9):
        add = k
        
        while len(str(ans_a)) < len(str(N)):
            if add + i <= 9 and add + i >= 0:
                add = add +i
                ans_a = ans_a *10 + add
            else:
                break
        if ans_a >= N:
            print(ans_a)
            exit()
        ans_a = k
```
# 解説
- ポイントは全探索するとしてもそこまでの計算量にはならないということである。
- まず2桁以下であればそれがそのまま答えになる
- 11桁以上(9876543210が最大の等差数列)の場合は同じ数の羅列になるためその場合分けを行う
    - (12222222222222の時は222222222222222が答えだし211111111111111の時は22222222222222222が答えというように必ずしも１の位がおんなじになるわけではないから場合わけ)
    - 先頭が9だった場合は必ず答えは9の羅列になるのでそこも場合わけ
- あとは均等な等差の数を追加して✖️10をするということを繰り返していくだけで答えを得ることができる。