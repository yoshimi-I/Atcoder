X,K,D = map(int,input().split())
#検算関数
# import random
# import debug
# X=random.randint(-10000,10000)
# K=random.randint(1,500)
# D=random.randint(1,10000)
# print("X=",X,"K=",K,"D=",D)    
# print(debug.solver(X,K,D))
X = abs(X)    
ans_1 = X%D    
ans_2 = abs(ans_1-D)
count =0
if X- K*D >= ans_1:
    print(X- K*D)
    exit()
else:
    count_1 = int((X - ans_1)/D)
    remain_count = (K - count_1)%2
    if remain_count == 0:
        print(ans_1)
        exit()
    else:
        print(ans_2)
        exit()
