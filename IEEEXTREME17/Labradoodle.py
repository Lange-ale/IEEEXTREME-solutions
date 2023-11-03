prex = {} 
sufx = {}
composite = []
n, m = map(int, input().split())
for i in range(n):
    w = input()
    if len(w) < 3: continue
    if w[:3] not in prex:
        prex[w[:3]] = []
    prex[w[:3]].append(w)
    if w[-3:] not in sufx:
        sufx[w[-3:]] = []
    sufx[w[-3:]].append(w)
    
for i in range(m):
  composite.append(input())
 
 
# n, m = 6, 7
# words =  [
# "spoon",
# "fork",
# "labrador",
# "poodle",
# "form",
# "car"
# ]
# composite = [
# "spork",
# "labradoodle",
# "fordle",
# "cardor",
# "lark",
# "spoooon",
# "labradabrador"
# ]

def get_word(comp):
    n_letters = 3
    try:
        prex_poss = prex[comp[:n_letters]]
        sufx_poss = sufx[comp[-n_letters:]]
    except KeyError:
        return -1
    
    toRet = ""
    for prex_p in prex_poss:
        for sufx_p in sufx_poss:
            i = n_letters - 1
            j = - n_letters
            finish = True
            while finish and i < len(comp) + j + 1 :
                finish = False
                if i < len(prex_p) and prex_p[i] == comp[i]: 
                    i += 1
                    finish = True
                try:
                    if sufx_p[j] == comp[j]: 
                        j -= 1
                        finish = True
                except:
                    j += 1
                
            if i -1 >= len(comp) + j :
                if toRet != "": 
                    return -2
                toRet = prex_p + " " + sufx_p
                
    if toRet =="":
        return -1
    return toRet    
               
for comp in composite:
  word = get_word(comp)
  if word == -1:
    print("none")
  elif word == -2:
    print("ambiguous")
  else:
    print(word)