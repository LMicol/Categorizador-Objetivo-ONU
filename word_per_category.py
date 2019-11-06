from MinerUtils import MinerUtils as Mu
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import operator


original = pd.read_excel("tabelas/final.xlsx")
original = original[['TITULO_PROJETO','PALAVRAS_CHAVE','RESUMO','OBJETIVO_ONU']]

alltxt = []
for i in range (17):
    alltxt.append("")
    
for i in range(3):
    for j in range(2351):
        classific = original.iloc[j,3] - 1
        x = original.iloc[j, i]
        if(x != -1):
            alltxt[classific] += x
            alltxt[classific] += ' '

for i in range(17):
    alltxt[i] = alltxt[i].lower()
    alltxt[i] = Mu.removeall(alltxt[i])


dictis = []
for i in range(17):
    dictis.append(Mu.counter(alltxt[i]))

final_dict = []
for i in range(17):
    tuples = dictis[i].items()
    tuples = tuple(x for x in tuples if (not(x[0].isdigit())) )
    final_dict.append(tuples)

for i in range(17):
    list_tuples = []
    for item in final_dict[i]:
        list_tuples.append(item)
    list_tuples.sort(key=operator.itemgetter(1))
    
    labels = []
    values = []
    while( (len(labels) < 25) and (len(list_tuples) > 1) ):
        a = list_tuples.pop()
        if((len(a[0]) > 2)):
            labels.append(a[0])
            values.append(a[1])
    
    
    index = np.arange(len(labels))    
    plt.bar(index, values)    
    plt.xlabel('Palavra', fontsize=2)
    plt.ylabel('Repetições', fontsize=2)
    plt.xticks(index, labels, fontsize=10, rotation=90)
    plt.show()