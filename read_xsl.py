import pandas as pd
from pandas import read_excel

''' ## '''

def read_resume(Path, Table, Column):
    file = Path
    Tabela_Treina = pd.ExcelFile(file).parse(Table)
    
    Coluna_Resumo = Tabela_Treina[[Column]]

    return Coluna_Resumo

''' ## '''

def count_words(data):
    array = {}

    for word in data:
        if(word != ' '):
            if(array[word] == null):
                array[word] = 0
            else:
                array[word] += 1

    return array


''' ## '''

def main():
    resumo = read_resume('Projetos_CC.xlsx','Treina', 'RESUMO')
    string_resumo = resumo.to_string();
    test = count_words(string_resumo)
    print (test)


''' ## '''

if __name__ == '__main__':
    main()
