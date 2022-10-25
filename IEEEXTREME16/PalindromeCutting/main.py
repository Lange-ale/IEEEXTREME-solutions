import math

entry = input().split()
N = int(entry[0])
M = int(entry[1])
ans = M + 2 * math.factorial(M)
print(ans)


