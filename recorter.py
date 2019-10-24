'''  not used '''


import matplotlib.pylab as plt
import pandas as pd

def remove_all_trash(s):
    s = s.replace(",", " ")
    s = s.replace("-", " ")
    s = s.replace(".", " ")
    s = s.replace(":", " ")
    s = s.replace("(", " ")
    s = s.replace(")", " ")
    s = s.replace("'", " ")
    s = s.replace("/", " ")
    s = s.replace("[", " ")
    s = s.replace("]", " ")
    s = s.replace("?", " ")
    s = s.replace("!", " ")
    s = s.replace("=", " ")
    s = s.replace("\"", " ")    
    s = s.replace("\\", " ")
    
    return s


def counting_words(s):
    dicio = dict()
    lista = s.split(" ")
    
    for palavra in lista:
        try:
            dicio[palavra] += 1
        except:
            dicio[palavra] = 1
            
    return dicio
    

data = pd.read_excel("tabelas/final.xlsx")
text_label = ["TITULO_PROJETO","PALAVRAS_CHAVE","RESUMO"]
X = data[text_label]

big_string = ""

for i in range(3):
    for j in range(2351):
        a = X.iloc[j,i]
        if(a != -1):
            big_string += " "
            big_string += a

big_string = remove_all_trash(big_string)
big_string = big_string.lower()

dicio = counting_words(big_string)

lists = sorted(dicio.items())
x, y = zip(*lists)
plt.plot(x, y)
plt.show()







