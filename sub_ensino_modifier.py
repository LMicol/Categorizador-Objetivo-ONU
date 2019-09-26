import pandas as pd

def refact(excel_table, column):
    return excel_table[[column]]
    
def numeric_string(s, i):
    num = ''
    for j in range(0, i):
        if(s[j] != '.'):
            num = num + s[j]
    return num    

def create_dataframe(lista):
    df = pd.DataFrame(columns=['SUBUNIDADE_ENSINO'])
    for i in lista:
        df = df.append({'SUBUNIDADE_ENSINO' : i}, ignore_index=True)
    return df

''' SCRIPT PARA CONVERSÃO DOS VALORES DA COLUNA SUBUNIDADE DE ENSINO '''

original = pd.read_excel("tabelas/data.xlsx")
ue = refact(original, "SUBUNIDADE_ENSINO")

f = open("tabelas/unidade_de_ensino_ref.txt", "w+")

numerics = []

for i in range(0,ue.shape[0]):
    s = ue.iloc[i][0]
    subs = s[0:15]
    subs = numeric_string(subs, 15)
    numeric = int(subs)
    numerics.append(numeric)
    nome = s[18:]
    f.write(str(numeric) + ' - ' + nome)

f.close()    
dataframe = create_dataframe(numerics)
original["SUBUNIDADE_ENSINO"] = dataframe["SUBUNIDADE_ENSINO"].values
original.to_excel("final.xlsx", engine = 'openpyxl')


