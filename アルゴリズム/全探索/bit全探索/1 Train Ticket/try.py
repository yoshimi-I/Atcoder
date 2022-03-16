N = input()
for i in range(2**3):
    L = ["+","+","+"]
    for j in range(3):
        if (i>>j) & 1:
            L[j] = "-"
    if eval(N[0]+L[0]+N[1]+L[1]+N[2]+L[2]+N[3]) == 7:
        print(N[0]+L[0]+N[1]+L[1]+N[2]+L[2]+N[3]+"=7")
        break
