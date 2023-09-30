

def qual_mais_recente(dia_data_um, mes_data_um, ano_data_um, dia_data_dois, mes_data_dois, ano_data_dois):

    tempo_total_em_dias_um = (ano_data_um*365) + mes_data_um*(30.42) + dia_data_um
    tempo_total_em_dias_dois = (ano_data_dois*365) + mes_data_dois*(30.42) + dia_data_dois

    condicao = tempo_total_em_dias_dois > tempo_total_em_dias_um

    if(condicao):
        return condicao
    else:
        return condicao

def main():
    dia_data_um = int(input())
    mes_data_um = int(input())
    ano_data_um = int(input())

    dia_data_dois = int(input())
    mes_data_dois = int(input())
    ano_data_dois = int(input())

    resultado = qual_mais_recente(dia_data_um, mes_data_um, ano_data_um, dia_data_dois, mes_data_dois, ano_data_dois)

    if(resultado):
        print(f'{dia_data_dois}/{mes_data_dois}/{ano_data_dois}')
    elif(not resultado):
        print(f'{dia_data_um}/{mes_data_um}/{ano_data_um}')
    else:
        print('Entrada de dados incorreta')



if __name__ == '__main__':
    main()