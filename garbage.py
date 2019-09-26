import pandas as pd
from pandas import read_excel

'''
        Ferramenta para classificação automatica de projetos com base na especificação da ONU
    Os dados de teste são as tabelas de projetos da UFSM, uma RNA identifica os padrões e classifica os projetos 
    com base nos dados discritos 

    To do:
    - Criação da RNA para classificação
    - Treinamento dos dados
    
    
    Done:
    - Limpar "lixo" da tabela de dados
    - Garimpar dados para deixar a tabela só com os dados importantes
    - Contar palavras da coluna de Resumo



'''



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
    raw_data = pd.read_excel('tabelas/Tabela_dados.xlsx')
    print(raw_data)
    '''
    resumo = read_resume('Projetos_CC.xlsx','Treina', 'RESUMO')
    string_resumo = resumo.to_string();
    test = count_words(string_resumo)
    print (test)
    '''

''' ## '''

if __name__ == '__main__':
    main()
