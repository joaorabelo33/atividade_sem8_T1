
def armazena_data_em_dias(dia, mes, ano):
    tempo_total = (ano*365) + mes*(30.42) + dia
    
    return tempo_total

def calcula_idade(dia, mes, ano, dia_nascimento, mes_nascimento, ano_nascimento):
    idade = (armazena_data_em_dias(dia, mes, ano) - armazena_data_em_dias(dia_nascimento, mes_nascimento, ano_nascimento))//365
   
    return int(idade)

def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())

    dia_nascimento = int(input())
    mes_nascimento = int(input())
    ano_nascimento = int(input())

    print(calcula_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento))


if __name__ == '__main__':
    main()