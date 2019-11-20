from sklearn.ensemble import RandomForestClassifier
from MinerUtils import MinerUtils as Mu
from appJar import gui
import pandas as pd
import numpy as np
import pickle


classifier = None
words_list = list()
unidades_list = list()
unidades = dict()
onu_obj = dict()


def getXY(dataset):
    columns = np.array(dataset.columns)
    out = np.array(['OBJETIVO_ONU'])
    inputs = np.setdiff1d(columns, out)

    X = dataset[inputs]
    y = dataset[out]
    y = y[y.columns[0]].values

    return X, y

def load_data():

    global classifier
    classifier = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                   max_depth=None, max_features='auto', max_leaf_nodes=None,
                   min_impurity_decrease=0.0, min_impurity_split=None,
                   min_samples_leaf=1, min_samples_split=7,
                   min_weight_fraction_leaf=0.0, n_estimators=30, n_jobs=-1,
                   oob_score=False, random_state=123, verbose=0,
                   warm_start=False)

    ds = pd.read_excel('tabelas/dataset_definitivo.xlsx').dropna()
    X, y = getXY(ds)
    classifier = classifier.fit(X, y)

    with open('obj/UniEns.dict', 'rb') as f:
        global unidades
        unidades = pickle.load(f)

    with open('obj/UniEns.list', 'rb') as f:
        global unidades_list
        unidades_list = pickle.load(f)

    with open('obj/words.list', 'rb') as f:
        global words_list
        words_list = pickle.load(f)

    with open('obj/onu_obj.dict', 'rb') as f:
        global onu_obj
        onu_obj = pickle.load(f)


def handler_text():
    ''' Agrupa t\odo texto em um só e já cria a tabela com os dados necessários '''
    texto = app.entry("Título do projeto") + ' '
    texto += app.entry("Título do projeto") + ' '
    texto += app.entry("Título do projeto")
    texto = Mu.removeall(texto)
    texto = texto.lower()

    palavras = texto.split(' ')

    dici = {}

    for w in words_list:
        dici[w] = 0

    for p in palavras:
        try:
            dici[p] += 1
        except:
            None

    alpha = pd.DataFrame.from_dict(dici, orient='index')
    return alpha.T

def handler_numeric():
    ''' numeros guarda os valores numericos do classificador '''
    numeros = []

    # Número de alunos envolvidos
    numeros.append(app.getEntry("Número de alunos envolvidos"))

    # Classificação
    c = app.getOptionBox("Classificação")
    if(c == 'Ensino'):
        numeros.append(1)
    elif(c == 'Pesquisa'):
        numeros.append(2)
    elif (c == 'Extensão'):
        numeros.append(3)

    # Número do público alvo
    numeros.append(app.getEntry("Número do público alvo"))

    # Unidade de Ensino
    UE = app.getOptionBox("Unidade de Ensino")
    numeros.append(unidades[UE])

    alpha = pd.DataFrame(numeros)
    return alpha.T


def handler():
    try:
        n = handler_numeric()
        p = handler_text()

        user_inputs = pd.concat([n, p], axis=1)
        resposta = classifier.predict(user_inputs)

        app.infoBox("Resultado da Classificação", onu_obj[resposta[0]], parent=None)
    except:
        app.errorBox("ERROR", 'Algo deu errado', parent=None)

load_data()
with gui("Classificador de objetivos ONU", "900x600", bg='white', font={'size': 15}) as app:
    app.entry('Título do projeto', label=True, focus=True)
    app.entry('Resumo', label=True, focus=True)
    app.entry('Palavras-chave', label=True, focus=True)
    app.entry("Número de alunos envolvidos", label=True, focus=True)
    app.entry("Número do público alvo",label=True, focus=True)
    app.addLabelOptionBox('Classificação', ['Ensino','Pesquisa','Extensão'] )
    app.addLabelOptionBox("Unidade de Ensino", unidades_list)
    app.buttons(["Classificar"], [handler])
