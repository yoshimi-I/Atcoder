from fractions import Fraction
N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
for i in range(N):
    x_1 = L[i][0]
    y_1 = L[i][1]
    for j in range(i+1,N):
        x_2 = L[j][0]
        y_2 = L[j][1]
        for k in range(j+1,N):
            x_3 = L[k][0]
            y_3 = L[k][1]
            if x_1==x_2 :
                if x_3 == x_1:
                    print("Yes")
                    exit()
                else:
                    continue
            if x_1==x_3:
                if x_2 == x_1:
                    print("Yes")
                    exit()
                else:
                    continue
            if x_2==x_3:
                if x_1 == x_2:
                    print("Yes")
                    exit()
                else:
                    continue
            Y = y_2-y_1 
            X = x_2-x_1
            slope = Fraction(Y,X)
            if slope*(x_3-x_1) + y_1 == y_3:
                print("Yes")
                exit()
            else:
                continue
print("No")            


