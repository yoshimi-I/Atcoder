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