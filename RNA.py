import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score


columns = ['prof','qt','fs','u0']
base = pd.read_excel('datasets/teste_dados_novos.xlsx')
X = base.iloc[:,0:-1].values
y = base['IC_Rob'].values

''' Conversão para terceira dimensão '''
from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)
y_dummy = np_utils.to_categorical(y)


def create_classifier():
    classifier = Sequential()
    classifier.add(Dense(units=3, activation='tanh', input_dim=??))
    classifier.add(Dropout(0.125))
    classifier.add(Dense(units=62, activation='tanh'))
    classifier.add(Dropout(0.125))
    classifier.add(Dense(units=17, activation='softmax'))
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    return classifier


classifier = KerasClassifier(build_fn=create_classifier, epochs=1000, batch_size=3000)
results = cross_val_score(estimator=classifier, X=X, y=y, cv=10, scoring='accuracy')
media = results.mean()
desvio = results.std()

teste = pd.read_excel('datasets/dados_validação.xlsx')
X_compare = teste.iloc[:,:].values

respostas = []
aux = 0;
for i in X_compare:
    respostas[aux] = classifier.predict(i)
    aux += 1















