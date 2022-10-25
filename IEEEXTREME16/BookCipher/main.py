def findLetter(grid, c, pos):
    if pos == 'S':
        for k in range(len(grid)):
            for l in range(len(grid[k])):
                if grid[k][l] == c:
                    i = k
                    j = l
                    return [i + 1, j + 1]
    for k in range(len(grid)):
        for l in range(len(grid[k])):
            if grid[-k - 1][-l - 1] == c:
                i = len(grid) - k
                j = len(grid[k]) - l
                return [i, j]
    return [-1, -1]


# queue<string> phrases, XML;
chiper = []
phrases = []
XML = []
p = int(input())
n = int(input())
entry = input().split(",")
R = int(entry[0])
C = int(entry[1])
grid = [[]]
pos = input()
for i in range(p):
    phrases.append(input())
for i in range(n):
    XML.append(input())

i = j = 0
while i < R and j < C and len(XML) > 0:
    temp = XML.pop(0)
    k = 0
    while k < len(temp):
        if temp[k] == '<':
            while temp[k] != '>':
                k += 1
        else:
            grid[i].append(temp[k] if temp[k] != ' ' else '_')
            j += 1
            if j == C:
                j = 0
                i += 1
                if i == R:
                    break
                grid.append([])
        k += 1

positions = {}
while len(phrases) > 0:
    phrase = phrases.pop(0)
    chiper.append("")
    for c in phrase:
        if c not in positions:
            positions[c] = findLetter(grid, c, pos)
        if positions[c][0] == -1:
            chiper[-1] = "0 "
            break
        chiper[-1] += str(positions[c][0]) + "," + str(positions[c][1]) + ","
    chiper[-1] = chiper[-1][:-1]

for i in range(len(chiper)):
    print(chiper[i])
