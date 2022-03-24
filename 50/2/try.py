from collections import deque


from collections import deque
A = list(input())
A = deque(A)
c = A.popleft()
A.append(c)
A=''.join(A)
print(A)
