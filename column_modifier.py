import pandas as pd
import MinerUtils as Mu

init = pd.read_excel("tabelas/final.xlsx")

label = []
label.append(["clima", "climático", "climática", "climáticas"])
label.append(["mulher", "mulheres", "feminismo"])
label.append(["violência", "violento", "violar", "violação"])
label.append(["pesquisa", "pesquisar", "pesquisando"])
label.append(["brasil", "brasileiro", "brasileira"])
label.append(["social", "socialização", "socialidade", "socializar", "sociável", "socializando"])
label.append(["comunicação", "comunicatividade", "comunicar"])
label.append(["informação", "informações", "informatívo"])
label.append(["qualidade", "qualidades"])
label.append(["ensino", "ensinar", "ensinamento", "ensinando"])
label.append(["estudo", "estudos", "estudar", "estudando"])
label.append(["ambiental", "ambiente", "ambientalismo", "ambientalção"])
label.append(["produção", "produzir", "produzindo", "produtividade"])
label.append(["adolescentes", "adolescente"])
label.append(["espécies", "espécie"])
label.append(["dados", "dado"])
label.append(["água"])
label.append(["desenvolvimento","desenvolvimentos","desenvolver","desenvolvendo"])

y = init["OBJETIVO_ONU"]
X = init[['ALUNOS_ENVOLVIDOS', 'CLASSIFICACAO', 'NUM_PUB_ALVO','SUBUNIDADE_ENSINO', 'NIVEL_ESCOLARIDADE', 'DOMI_RESIDENCIA']]

    
text_frame = init[["TITULO_PROJETO","PALAVRAS_CHAVE","RESUMO"]]

new_columns = pd.DataFrame(columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

for num in range(2351):
    text = ""
    new_labels = []
    for i in range(len(label)):
        new_labels.append(0)

    for j in range(3):
        if (text_frame.iloc[num,j] != -1):
            text += text_frame.iloc[num,j]
            text += " "
    text = text.lower()
    text = Mu.MinerUtils.removeall(text)
    t_list = text.split(' ')
    
    for t in t_list:
        for l in label:
            for word in l:
                if(t == word):
                    new_labels[label.index(l)] += 1
    t_list = []
                    
    new_columns = new_columns.append(pd.Series(new_labels, index=new_columns.columns), ignore_index=True)
        
alpha = pd.concat([X, new_columns], axis=1)
alpha.to_excel("tabelas/data_new.xlsx",  engine = 'openpyxl')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                