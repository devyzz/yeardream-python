from collections import deque

n, k = map(int, input().split())
numbers = deque([i for i in range(1,n+1)])
result = []

while numbers:
    for i in range(k-1):
        numbers.append(numbers.popleft())
    result.append(numbers.popleft())

print(result)