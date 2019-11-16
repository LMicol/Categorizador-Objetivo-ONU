from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import pickle
import sys


'''
    Random Forest foi o classificador escolhido após ter apresentado os melhores
    resultados nos teste de classificação
'''
def RFClassifier(X, y):
    rfc = RandomForestClassifier()
    params = {'criterion':['gini'],
          'n_estimators':[30],
          'min_samples_leaf':[1],
          'min_samples_split':[7], 
          'random_state':[123],
          'n_jobs':[-1]}
    
    return gridSearch(rfc, params, X, y)

# Validação cruzada para o classificador
def gridSearch(model, params, X, y):
    model1 = GridSearchCV(model, param_grid=params, n_jobs=-1, cv=3)
    model1.fit(X, y)
    #print("Best Hyper Parameters:", model1.best_params_)
    #print("Estimator Params:", model1.best_estimator_)

    return model1.best_estimator_


# função de normalização dos dados
def normalize(X):
    X_norm = (X-X.min())/(X.max()-X.min())
    return X_norm

#função de separalão do dataset
def getXY(dataset):
    columns = np.array(dataset.columns)
    out = np.array(['OBJETIVO_ONU'])
    inputs = np.setdiff1d(columns,out)

    X = dataset[inputs]
    y = dataset[out] #.iloc[:]
    
    return X,y


def main(argv):
    # leitura e separação das colunas
    ds = pd.read_excel('../MinerText/tabelas/data_new.xlsx').dropna()
    X,y = getXY(ds)
    
    
    # numero de classes calssificaveis e normalização das entradas
    y = y[y.columns[0]].values
    X_norm = normalize(X)

    # tranformação dos dados para utilização nos testes
    scaler = StandardScaler()
    scaler.fit(X)
    X_norm = scaler.transform(X)

    # separação dos dados para teste
    X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
    
    #classificador utilizado
    classifier = RFClassifier(X, y)
    classifier = classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)

    print('Prediction score [Random Forest]:')
    print(classifier.score(X_test, y_test))
    print(classification_report(y_test,y_pred))

    with open('randomforestclassifier.clf','wb') as f:
        pickle.dump(classifier, f)
        
    #classifier.preditc(value)

if __name__ == "__main__":
    main(sys.argv)
