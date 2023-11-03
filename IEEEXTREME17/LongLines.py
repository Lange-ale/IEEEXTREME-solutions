n, h0, a, c, q = map(int, input().split())
h_i = [ h0 ]
sum = 0
for i in range(1,n):
    h_i.append((a*h_i[-1]+c)%q)
    sum += len(h_i) - 1
    dim = len(h_i)-1
    for j in reversed(range(dim)):
        if h_i[j] <= h_i[-1]:
            h_i.pop(j)

print(sum)
