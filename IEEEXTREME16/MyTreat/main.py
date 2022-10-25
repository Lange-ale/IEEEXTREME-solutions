T = int(input())
for t in range(T):
    N = int(input())
    delta = {}
    piatti = 0
    giorni = 0
    for n in range(N):
        temp = input().split()
        who = temp[0]
        count = int(temp[1])
        to = temp[2:]
        #alice 2 bob dave
        if who not in delta.keys():
            delta[who] = count
        else:
            delta[who] += count
        for t in to:
            if t not in delta.keys():
                delta[t] = -1
            else:
                delta[t] -= 1
    giorni = max(delta.values())
    piatti = sum(x for x in delta.values() if x > 0)
    print(piatti, giorni)