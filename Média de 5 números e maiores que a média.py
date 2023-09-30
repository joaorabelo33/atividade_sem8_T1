

def media(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco):
    media = (valor_um + valor_dois + valor_tres + valor_quatro + valor_cinco)/5

    return media

def maiores_que_media(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco):
    media_geral = media(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco)
    if(valor_um > media_geral):
        print (f'{valor_um:.2f}')
    if(valor_dois > media_geral):
        print(f'{valor_dois:.2f}')
    if(valor_tres > media_geral):
        print(f'{valor_tres:.2f}')
    if(valor_quatro > media_geral):
        print(f'{valor_quatro:.2f}')
    if(valor_cinco > media_geral):
        print(f'{valor_cinco:.2f}')
    return '0.00'

def main():
    valor_um = int(input())
    valor_dois = int(input())
    valor_tres = int(input())
    valor_quatro = int(input())
    valor_cinco = int(input())   

    resultado_media = media(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco)

    print(f'{resultado_media:.2f}')
    maiores_que_media(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco)

if __name__ == '__main__':
    main()