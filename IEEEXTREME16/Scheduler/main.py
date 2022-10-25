entry = input().split()
N = int(entry[0])
workers = int(entry[1])
X = [int(i) for i in input().split()]

if workers == 1:
    total_sum = 0
    for i in X:
        total_sum = (total_sum + pow(2, i, 1000000007)) % 1000000007
    print(total_sum)
else:
    print(pow(2, max(X), 1000000007))

