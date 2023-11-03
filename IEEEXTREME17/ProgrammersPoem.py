m, n = input().split()
m = int(m)
n = int(n)	

nextLetter = 'A'

rhymeGroups = {}
for i in range(m):
	line = input()
	words = line.split()
	for word in words:
		rhymeGroups[word.lower()] = i
  
input()
  
last_words = []
for i in range(n):
	last_words.append(input().split()[-1].lower())
 
for i in range(n):
    if last_words[i] not in rhymeGroups:
        continue
    group = rhymeGroups[last_words[i]]
    found = False
    for j in range(n):
        if i!=j and last_words[j] in rhymeGroups and  group == rhymeGroups[last_words[j]]:
            found = True
            break
    if not found:
        last_words[i] = ""

groupLetters = {}

for i in range(n):
    word = last_words[i]
    if word in rhymeGroups:
        if rhymeGroups[word] not in groupLetters:
            groupLetters[rhymeGroups[word]] = nextLetter
            nextLetter = chr(ord(nextLetter) + 1) if nextLetter != 'X' else 'Y'
        print(groupLetters[rhymeGroups[word]], end='')
    else:
        print("X", end='')
  
"""
2 6
hash dash crash slash
underscore four

Waka waka bang splat tick tick hash
Caret quote back tick dollar dollar dash
Bang splat equal at dollar underscore
Percent splat waka waka tilde number four
Ampersand bracket bracket dot dot slash
Vertical bar curly bracket comma comma CRASH
"""