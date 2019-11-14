import sys
#import MLPMTuningClassifiers
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

import Feature_select as FL
import Normalization
import Tunning



def main(argv):
    classifiers=['RF','KNN','DT','SVM','RNA'] #,'nn','sgd']
    
    ds = pd.read_excel('../MinerText/tabelas/data_new.xlsx').dropna()

    X,y = FL.Selection(ds, ['OBJETIVO_ONU'])  #all_data = class_Rob / |||  output = IC_Rob / IC_Sch
    
    '''
    vet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(2267):
        vet[y.iloc[i][0]] += 1
    '''

    
    #todo pegar a quantidade de classes na saida
    y_size = 9  #no dataset 'output' são 6 classes
    #X = X[['ALUNOS_ENVOLVIDOS', 'CLASSIFICACAO', 'NUM_PUB_ALVO','SUBUNIDADE_ENSINO']]
    X_norm = Normalization.normalize(X)

    ### FEATURE SELECTION
    # two distinct ways to select features: kbest or fittoclassifier, which is better?
    #columns = FL.ExtraTree(X,y[y.columns[0]], number=5)
    #columns = FL.kBest(X_norm, y[y.columns[0]], k=5)
    #FL.corr_HeatMap(ds)

    #columns = ['Q','Qt','s1v0','fs','qc']#['Qt','fs','qc','qt','u2']#['qc', 'fs', 'u2']# ['Q','Qt','s1v0','fs','qc']#  'qc', 'fs', 'u2', 'sv0'#  'Qt','fs','qc','qt','u2'#

    #X = X[columns]
    y = y[y.columns[0]].values  # y[y.columns[0]].values

    #X_norm = Normalization.normalize(X)
    scaler = StandardScaler()
    scaler.fit(X)
    X_norm = scaler.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
    #clf = ''
    #clf = Tunning.DT(X_train, y_train)

    for cla in classifiers:
        print('>> GRIDSEARCH RUNNING on: ', cla)
        print()
        ###exec("clf = Tunning."+cla+"(X_train, y_train)")
        clf = Tunning.models(cla,X_train, y_train,y_size)
        ### PREDICTING
        y_pred = clf.predict(X_test)

        print("Prediction score [", cla,']:')
        print(clf.score(X_test, y_test))
        print(classification_report(y_test,y_pred))
        print('-------------------------------------------')
    # print score(y_test, y_pred)
    # print("Prediction r2 score: ",)
    # print(r2_score(y_test, y_pred))
    # precision, recall, fscore, support = score(y_test, y_pred)


    # Tuning classifier parameters
    # https://scikit-learn.org/stable/modules/grid_search.html
    #for cla in classifiers:
    #MLPMTuningClassifiers.get_parameters('knn', X, y)
        

if __name__ == "__main__":
    main(sys.argv)
