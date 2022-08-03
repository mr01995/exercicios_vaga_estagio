from json import load

with open ("dados.json", "r") as f:
    data = (load(f))

#descobrindo o menor valor de faturamento
def menor_valor():
    menor=9999999999
    for i in data:
        if i["valor"] < menor and i["valor"] != 0:
            menor = i["valor"]
    return menor

#descobrindo o maior valor de faturamento
def maior_valor():
    maior=0
    for i in data:
        if i["valor"] > maior and i["valor"] != 0:
            maior = i["valor"]
    return maior

#descobrindo dias em que o faturamento foi maior que a media mensal
def faturamento_acima_media():
    dias=0
    soma=0
    num_fat_maior=0
    for i in data:
        if i["valor"] != 0:
            soma += i["valor"]
            dias+=1
    media = soma / dias
    for i in data:
        if i["valor"] > media:
            num_fat_maior+=1
    return num_fat_maior


f.close()

if __name__=="__main__":

    print(f'Menor faturamento: {menor_valor()}')
    print(f'Maior faturamento: {maior_valor()}')
    print(f'Dias em que o faturamento foi maior que a média mensal: {faturamento_acima_media()}')