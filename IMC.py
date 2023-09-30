
def calculo_imc(peso, altura):
    imc = peso/altura**2
    return imc
def classifica_o_imc(peso, altura):
    valor_imc = calculo_imc(peso, altura)
    if(valor_imc < 18.5):
        return 'Abaixo do peso'
    elif(valor_imc < 25):
        return 'Peso normal'
    elif(valor_imc < 30):
        return 'Sobrepeso'
    elif(valor_imc < 35):
        return 'Obeso leve'
    elif(valor_imc < 40):
        return 'Obeso moderado'
    elif(valor_imc >= 40):
        return 'Obeso mórbido'
    else:
        raise ValueError('Entrada inválida')

def main():
    massa_do_individuo = float(input())
    altura_do_individuo = float(input())

    resultado_imc = calculo_imc(massa_do_individuo, altura_do_individuo)
    resultado = classifica_o_imc(massa_do_individuo, altura_do_individuo)
    print(f'{resultado_imc:.2f}')
    print(f'{resultado}')


if __name__ == '__main__':
    main()