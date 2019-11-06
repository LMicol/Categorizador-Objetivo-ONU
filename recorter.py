''' 
    ESTE ARQUIVO PEGA AS 100 PALAVRAS MAIS CITADAS ENTRE AS TRÊS COLUNAS DE 
    TEXTO E AS SALVA COMO DATASET, CONTA AS REPETIÇÕES POR LINHA E NO FINAL
    JUNTA COM A TABELA DO COMEÇO
'''
import pandas as pd
import operator
from MinerUtils import MinerUtils as Mu

original = pd.read_excel("tabelas/final.xlsx")
original = original[['TITULO_PROJETO','PALAVRAS_CHAVE','RESUMO', 'OBJETIVO_ONU']]

alltxt = ''

for i in range(3):
    for j in range(2351):
        classific = original.iloc[j,3] - 1
        x = original.iloc[j, i]
        if(x != -1):
            alltxt += x
            alltxt += ' '

alltxt = alltxt.lower()
alltxt = Mu.removeall(alltxt)


dc = Mu.counter(alltxt)

bad_words = ['que','para','com','como','dos','uma','das','dos','por','sobre',
             'entre','ser','são','serão','será','tem','nas','nos','não','sua',
             'seu','aos','este','através','bem','bom','mal','mau', 'mais', 
             'pela', 'assim', 'também', 'pelo', 'além', 'suas', 'cada', 'pode'
             'está', 'neste', 'nesta', 'parte', 'desta', 'deste', 'esta', 'este',
             'dessa', 'quais', 'ainda', 'tanto', 'isso', 'mesmo']

final_dict = {}
for item in dc:
    if(len(item) > 2):
        if (not(item[0].isdigit())):
            if (item not in bad_words):
                final_dict[item] = dc[item]

final_dict = sorted(final_dict.items(), reverse=True, key=operator.itemgetter(1))
fd100 = []
for i in range(100):
    fd100.append(final_dict[i])

word_list = []
for value in fd100:
    word_list.append(value[0])
#####################
data = pd.DataFrame(columns=word_list)

for i in range(2351):
    texto = ''
    for j in range (3):
        if (original.iloc[i][j] != -1):
            texto += original.iloc[i][j] + ' '
            
    texto = texto.lower()
    texto = Mu.removeall(texto)
    texto  = texto.split(' ')
    
    lista = []
    for j in range(100):
        lista.append(0)
    
    for j in range(100):
        for t in texto:
            if(t == word_list[j]):
                lista[j] += 1
    
    data.loc[i] = lista


original = pd.read_excel("tabelas/final.xlsx")
resposta = original[['OBJETIVO_ONU']]
original = original[['ALUNOS_ENVOLVIDOS', 'CLASSIFICACAO', 'NUM_PUB_ALVO','SUBUNIDADE_ENSINO', 'NIVEL_ESCOLARIDADE', 'DOMI_RESIDENCIA']]
alpha = pd.concat([original, data], axis=1)
alpha = pd.concat([alpha, resposta], axis=1)
alpha.to_excel("tabelas/data_new.xlsx",  engine = 'openpyxl')
























