

def qual_eh_maior(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco):
    maior = 0
    
    if(maior < valor_um ):
        maior = valor_um
    if(maior < valor_dois ):
        maior = valor_dois
    if(maior < valor_tres ):
        maior = valor_tres
    if(maior < valor_quatro ):
        maior = valor_quatro
    if(maior < valor_cinco ):
        maior = valor_cinco

    return maior

def qual_eh_menor(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco):
    menor = valor_um
    
    if(menor > valor_dois ):
        menor = valor_dois
    if(menor > valor_tres ):
        menor = valor_tres
    if(menor > valor_quatro ):
        menor = valor_quatro
    if(menor > valor_cinco ):
        menor = valor_cinco

    return menor

def main():
    valor_um = int(input())
    valor_dois = int(input())
    valor_tres = int(input())
    valor_quatro = int(input())
    valor_cinco = int(input())

    resultado_maior_numero = qual_eh_maior(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco)
    resultado_menor_numero = qual_eh_menor(valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco)

    print(f'{resultado_maior_numero}\n{resultado_menor_numero}')

if __name__ == '__main__':
    main()