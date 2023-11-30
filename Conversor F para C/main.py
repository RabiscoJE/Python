def celsius_to_fahrenheit(graus_c):
    graus_f = (graus_c * (9/5) + 32)
    return graus_f

def fahrenheit_to_celsius(graus_f):
    graus_c = (graus_f - 32) * 5/9
    return graus_c

def menu():
    print()
    print('[1] Celsius para Fahrenheit')
    print('[2] Fahrenheit para Celsius')

def main():
    temperatura = float(input('Digite a temperatura: '))
    menu()
    escolha = int(input('Escolha a opção: '))

    if escolha == 1:
        resultado = celsius_to_fahrenheit(temperatura)
        print(f'{temperatura}° em Celsius é equivalente a {resultado}° Fahrenheit.')
    if escolha == 2:
        resultado = fahrenheit_to_celsius(temperatura)
        print(f'{temperatura}° em Fahrenheit é equivalente a {resultado}° Celsius.')
    else:
        print('Escolha invalida!')

if __name__ == '__main__':
    main()