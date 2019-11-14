# -*- coding: utf-8 -*-

import pandas as pd
import operator
from MinerUtils import MinerUtils as Mu

original = pd.read_excel("tabelas/final sem algumas.xlsx")
y = original[['OBJETIVO_ONU']]
original = original[['TITULO_PROJETO','PALAVRAS_CHAVE','RESUMO', 'OBJETIVO_ONU']]

'''
vet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(2351):
   vet[y.iloc[i][0]] += 1
'''

vet_palavras = []
for i in range(17):
    vet_palavras.append("")


for i in range(2146):
    txt = ''
    for j in range(3):
        t = original.iloc[i,j]
        if(t != -1):
            txt += t
            txt += ' '
    vet_palavras[original.iloc[i,3]] += txt
    

dicts = []
for i in range(17):
    vet_palavras[i] = Mu.removeall(vet_palavras[i])
    vet_palavras[i] = vet_palavras[i].lower()
    dicts.append(Mu.counter(vet_palavras[i]))
    

bad_words = ['que','para','com','como','dos','uma','das','dos','por','sobre',
             'entre','ser','são','serão','será','tem','nas','nos','não','sua',
             'seu','aos','este','através','bem','bom','mal','mau', 'mais', 
             'pela', 'assim', 'também', 'pelo', 'além', 'suas', 'cada', 'pode'
             'está', 'neste', 'nesta', 'parte', 'desta', 'deste', 'esta', 'este',
             'dessa', 'quais', 'ainda', 'tanto', 'isso', 'mesmo', 'santa',
             'maria', 'uso', 'ufsm', 'sendo', 'partir']

final_dicts = []
for i in range(17):
    final_dicts.append({})

i = 0
for dc in dicts:
    for item in dc:
        if(len(item) > 2):
            if (not(item[0].isdigit())):
                if (item not in bad_words):
                    final_dicts[i][item] = dc[item]
    i += 1
    
i = 0
for d in final_dicts:
    if (d != {}):
        final_dicts[i] = sorted(final_dicts[i].items(), reverse=True, key=operator.itemgetter(1))
    i += 1

new_words = []
for i in range(17):
    if (final_dicts[i] != {}):
        j = 0
        while j != 30:
            new_words.append(final_dicts[i][j][0])
            j += 1

new_words = list(set(new_words))

###################################
    
data = pd.DataFrame(columns=new_words)

for i in range(2146):
    texto = ''
    for j in range (3):
        if (original.iloc[i][j] != -1):
            texto += original.iloc[i][j] + ' '
            
    texto = texto.lower()
    texto = Mu.removeall(texto)
    texto  = texto.split(' ')
    
    lista = []
    for j in range(len(new_words)):
        lista.append(0)
    
    for j in range(len(new_words)):
        for t in texto:
            if(t == new_words[j]):
                lista[j] += 1
    
    data.loc[i] = lista


original = pd.read_excel("tabelas/final sem algumas.xlsx")
resposta = original[['OBJETIVO_ONU']]
original = original[['ALUNOS_ENVOLVIDOS', 'CLASSIFICACAO', 'NUM_PUB_ALVO','SUBUNIDADE_ENSINO']]
alpha = pd.concat([original, data], axis=1)
alpha = pd.concat([alpha, resposta], axis=1)
alpha.to_excel("tabelas/data_new.xlsx",  engine = 'openpyxl')
    
            