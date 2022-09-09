import json

cens_lst = []

with open('censor.txt', encoding='utf-8') as f:
    for i in f:
        cens_lst.append(i.strip())

with open('censor.json', 'w', encoding='utf-8') as f:
    json.dump(cens_lst, f)

print(cens_lst)
