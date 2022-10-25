bestChar = [{} for i in range(8)]

with open('parole.txt', 'r') as f:
    words = f.read().splitlines()

for word in words:
    for i in range(len(word)):
        if word[i] not in bestChar[i]:
            bestChar[i][word[i]] = 0
        bestChar[i][word[i]] += 1
    for i in range(len(word), 8):
        if ' ' not in bestChar[i]:
            bestChar[i][' '] = 0
        bestChar[i][' '] += 1

weels = [sorted(my_dict, key=my_dict.get, reverse=True)[:11] for my_dict in bestChar]
for i in weels:
    for j in i:
        if j != ' ':
            print(j, end='')
    print()
