import itertools
ary = [1, 3, 5, 7, 9]
s = ['ab', 'bc', 'cd']
bi = [0,2,0,1,1,0,0,0,1,1,0,1,2,2,3,3,3]
P = [1,2,3]
C = [1,2,3,4,3,2,1]

##累積和
cumsum = itertools.accumulate(s)
print(list(cumsum))

## ある値が何個あるのか
gr = itertools.groupby(bi)
for k,i in gr:
    print(k,list(i))

## 順列
print(list(itertools.permutations(P)))

## 組み合わせ
print(list(itertools.combinations(C, 3)))