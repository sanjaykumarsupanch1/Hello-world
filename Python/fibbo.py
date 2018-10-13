import time

fibonacci = [1, 1]
n = int(input())
while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
for j in range(n):
    print(fibonacci[j], end=' ')
