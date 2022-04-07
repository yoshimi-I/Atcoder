A,B,W=map(int, input().split())  
W_g=W*1000
min_ans=10**15 
max_ans=-10**15
for X in range(1,10**6+10):
    if A*X<=W_g<=B*X:
        min_ans=min(min_ans,X)
        max_ans=max(max_ans,X)
if min_ans==10**15:
    print("UNSATISFIABLE")
else:
    print(min_ans,max_ans)