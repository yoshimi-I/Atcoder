# 解答
```
t = int(input())
def math(a):
    return (a**2)+(2*a)+3
ans = math(math(math(t)+t) + math(math(t)))
print(ans)
t = int(input())
def math(a):
    return (a**2)+(2*a)+3
ans = math(math(math(t)+t) + math(math(t)))
print(ans)
```
# 解説
- 特になし
- 関数を作ってそれを何回も呼び出す