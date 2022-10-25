T = int(input())
for t in range(T):
    entry = input()
    nums = entry.split(" ")[1:]
    answer = 1
    gradi = {}
    for n in nums:
        D = int(n) % 180
        if D < 0:
            D = 180 + D
        gradi[D] = 1
        
    print(len(gradi.keys()) * 2)