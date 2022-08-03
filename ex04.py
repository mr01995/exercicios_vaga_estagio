from xml.dom.expatbuilder import FragmentBuilder


list_dict = {"SP" :"67836.43","RJ" :"36678.66","MG" :"29229.88","ES" :"27165.48","Outros" :"19849.53"}


valores = [float(i) for i in list_dict.values()]

def main ():

    faturamento = faturamento_total()

    for ind, i in enumerate(valores):
        percentual = (i * 100) / faturamento
        if ind < 4:
            print(f'O percentual do {ind+1}º estado: {percentual:.2f}')
        else:
            print(f'O percentual dos demais estados: {percentual:.2f}')



def faturamento_total():
    faturamento = 0
    for i in valores:
        faturamento+=i
    return faturamento

if __name__=="__main__":
    
    main()

