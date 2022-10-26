import queue

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
    X.sort(reverse=True)
    pq = queue.PriorityQueue()
    for i in range(workers):
        pq.put(0)
    for i in X:
        tmp = pq.get()
        pq.put(tmp + pow(2, i))
    ans = 0
    while not pq.empty():
        ans = pq.get() % 1000000007
    print(ans)


