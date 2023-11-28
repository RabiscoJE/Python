def lucro_composto(c):
    investimento = 50
    lucro = 0
    odd = 2
    num_apostas = 10
    acerto = 6.5
    erro = 3.5

    for i in range(0, c):
        valor = investimento / num_apostas
        lucro = (valor * odd * acerto ) - (valor * odd * erro)
        investimento = (investimento /2) + lucro
    
    return lucro

def ganhos(investimento = 10, num_apostas = 10, odd = 2, percentual = 100):
    valor = investimento / num_apostas
    acerto = num_apostas * percentual / 100
    custo = num_apostas * valor
    ganho = (valor * odd * acerto ) #- custo
    
    print(f'''Acertando {acerto} de {num_apostas} 
          apostas com cada uma no valor de {valor} e odd de {odd}
          o ganho total será {ganho}''')

def lucro(investimento = 10, num_apostas = 10, odd = 2, percentual = 100):
    valor = investimento / num_apostas
    acerto = num_apostas * percentual / 100
    custo = num_apostas * valor
    ganho = (valor * odd * acerto )
    lucro = ganho - custo
    
    print(f'''Acertando {acerto} de {num_apostas} 
apostas com cada uma no valor de {valor} e odd de {odd}, o ganho será de {ganho} e
o lucro final será {lucro}''')

def lucro_max_min(odds: list, erros = 0):
    odds = sorted(odds)
    ganho_max = 0
    ganho_min = 0

    # melhor caso
    for i in range(erros, len(odds)):
        ganho_max += odds[i]
        print(odds[i])

    print()

    # pior caso
    for i in range(0, len(odds) - erros):
        ganho_min += odds[i]
        print(odds[i])
    
    print(f'No melhor dos casos, errando {erros} palpites, você ganharia {ganho_max} o valor da aposta')
    print(f'No pior dos casos, errando {erros} palpites, você ganharia {ganho_min} o valor da aposta')

lucro(10, 10, 1.4, 70)

lista = [1.7, 1.4, 1.6, 2.2, 2.3, 1.6, 2, 1.4, 1.5, 1.6]
lucro_max_min(lista, 2)