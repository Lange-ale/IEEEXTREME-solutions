#takes 5.26/100 points

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import xml.etree.ElementTree as ET

docu = ''
while True:
    try:
        x = input()
        docu += x
        if x == '</Thesaurus>':
            break
    except:
        break


root = ET.fromstring(docu)

top_terms = []
terms = {}
synonims = {}
real_names = {}

for info in root.findall('TermInfo'):
    t = info.find('T').text.lower()
    
    if t not in terms:
        terms[t] = {
            'bt': [],
            'nt': []
        }
    
    ufs = info.findall('UF')
    nts = info.findall('NT')
    bts = info.findall('BT')
    
    if len(ufs) != 0:
        for uf in ufs:
            text = uf.text.lower()
            synonims[text] = t
    
    if len(bts) == 0:
        top_terms.append(t)
        real_names[t] = info.find('T').text
    else:
        for bt in bts:
            text = bt.text.lower()
            if text in synonims:
                terms[t]['bt'].append(synonims[text])
            else:
                terms[t]['bt'].append(text)

    if len(nts) != 0:
        for nt in nts:
            text = nt.text.lower()
            if text in synonims:
                terms[t]['nt'].append(synonims[text])
            else:
                terms[t]['nt'].append(text)


def explore(top):
    cont = 1
    for nt in top['nt']:
        if nt not in terms:
            continue
        cont += explore(terms[nt])
    return cont

to_write = []
for top in top_terms:
    ans = explore(terms[top])
    to_write.append((ans, top))
    
to_write.sort(reverse=True)
for t in to_write:
    print(f'{real_names[t[1]]} = {t[0]}')