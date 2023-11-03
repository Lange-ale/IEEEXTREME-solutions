rumorsFrom = {}
uniqueValues = set()
pending = []

N = int(input())
for _ in range(N):
    line = input().split()
    if line[1] == '->':
        rumorsFrom[line[2]] = line[0]
        uniqueValues.add(line[0])
    else:
        pending.append((line[0], line[2]))

updated = True
while updated and pending:
    updated = False
    i = 0
    while i < len(pending):
        p = pending[i]
        if p[0] in rumorsFrom:
            rumorsFrom[p[1]] = rumorsFrom[p[0]]
            updated = True
            pending.pop(i)
        elif p[1] in rumorsFrom:
            rumorsFrom[p[0]] = rumorsFrom[p[1]]
            updated = True
            pending.pop(i)
        else:
            i += 1

people = set()
for i in pending:
    people.add(i[0])
    people.add(i[1])

people.update(uniqueValues.difference(rumorsFrom.keys()))

for person in sorted(people):
    print(person)
