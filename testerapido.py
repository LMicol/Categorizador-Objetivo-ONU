# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestClassifier
from MinerUtils import MinerUtils as Mu
import numpy as np
import pandas as pd
import pickle


def getXY(dataset):
    columns = np.array(dataset.columns)
    out = np.array(['OBJETIVO_ONU'])
    inputs = np.setdiff1d(columns, out)

    X = dataset[inputs]
    y = dataset[out]  # .iloc[:]

    return X, y


with open('obj/words.list','rb') as f:
    lista = pickle.load(f)
    
titulo = 'sul Virtualização e Colocação de Funções para Descoberta de Conhecimento e Automação de Processos área extensão'
resumo = 'Tecnologias recentes como Internet das Coisas, Cidades Inteligentes e crowdsourcing estão gerando quantidades significativas de dados. Identificar padrões, compreender e extrair conhecimentos desses dados são, atualmente, importantes desafios de pesquisa. O processo de Descoberta de Conhecimento em Banco de Dados permite a descoberta de informações em base de dados através de uma cadeia de atividades bem definida. Técnicas de Aprendizagem de Máquina permitem a criação de modelos capazes de identificar padrões e extrair conhecimento dos dados. A aplicação de virtualização de funções oferece uma nova forma de projetar, implantar e gerenciar serviços computacionais em qualquer hardware, eliminando limitações impostas por tecnologias proprietárias. Este projeto visa agregar esses três artifícios computacionais para desenvolver um arcabouço que possibilite a virtualização e colocação de funções que permitam a descoberta de conhecimento, visando a automação e modelagem de processos.'
palavras_chave = 'mineração de dados, aprendizagem de máquina, modelagem de processos, automação de processos'

total = titulo + ' ' + resumo + ' ' + palavras_chave
total = Mu.removeall(total)
total = total.lower()
r = total.split(' ')

dici = {}

for a in lista:
    dici[a] = 0
    
for t in r:
    try:
        dici[t] += 1
    except:
        None
        
alpha = pd.DataFrame.from_dict(dici, orient='index')
alpha = alpha.T

classificador = RandomForestClassifier()
f = open('obj/randomforestclassifier.clf','rb')
classificador = pickle.load(f)
f.close()

ds = pd.read_excel('tabelas/dataset_definitivo.xlsx').dropna()
X, y = getXY(ds)
y = y[y.columns[0]].values

#print(classificador)
classificador.fit(X, y)

A = pd.DataFrame([4,2,1000,858000000])
A = A.T

alpha = pd.concat([A, alpha], axis=1)

um = classificador.predict(alpha)
print(type(um[0]))

dicionario = {}

dicionario[1]  = 'Erradicação da pobreza'
dicionario[2]  = 'Fome zero e agricultura sustentável'
dicionario[3]  = 'Saúde e bem-estar'
dicionario[4]  = 'Educação de Qualidade'
dicionario[5]  = 'Igualdade de gênero'
dicionario[6]  = 'Água potável e saneamento'
dicionario[7]  = 'Energia limpa e acessível'
dicionario[8]  = 'Trabalho decente e crescimento econômico'
dicionario[9]  = 'Indústria, inovação e infraestrutura'
dicionario[10] = 'Redução das desigualdades'
dicionario[12] = 'Cidades e comunidades sustentáveis'
dicionario[13] = 'Ação contra a mudança global do clima'
dicionario[14] = 'Vida na água'
dicionario[15] = 'Vida Terrestre'
dicionario[16] = 'Paz, justiça e instituições eficazes'
dicionario[17] = 'Parcerias e meio de Implementação'

f = open('onu_obj.dict','wb')
pickle.dump(dicionario, f)























