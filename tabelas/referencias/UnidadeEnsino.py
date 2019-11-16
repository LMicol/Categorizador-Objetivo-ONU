import operator
import pickle
from appJar import gui

file = open("unidade_de_ensino.txt")

linhas = file.readlines()
linhas = linhas[0]

subs = {}

codigo = ''
unidade = ''
flag = False

i = 0
while (i != 546184):    
    try:
        n = int(linhas[i])
        codigo += linhas[i] 
    except:
        try:
            n = int(linhas[i+1])
            n_unidade = ''
            for j in range(len(unidade)):
                n_unidade += unidade[j]
                if(unidade[j+1] == ' '):
                    if(unidade[j+2] == ' '):
                        n_unidade += unidade[j+1]
                        break
            subs[codigo] = n_unidade[3:-1]
            unidade = ''
            codigo = ''
        except:
            unidade += linhas[i]
    i += 1
    
subs = {y:x for x,y in subs.items()}

subs_list = sorted(subs.items(), key=operator.itemgetter(0))
for i in range(len(subs_list)):
    subs_list[i] = subs_list[i][0]

'''    
with open('UniEns.list','wb') as f:
    pickle.dump(subs_list, f)

with open('UniEns.dict','wb') as f:
    pickle.dump(subs, f)    
'''