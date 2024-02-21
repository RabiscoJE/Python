def is_primo(num: int) -> bool:
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    divisor = 3
    while divisor <= num // 2:
        if num % divisor == 0:
            return False
        divisor += 2

    return True

def main():
    numero = int(input('Digite um número que você queira descobrir se é primo: '))
    if is_primo(numero):
        print(f'O número {numero} é primo!')
    else: 
        print(f'O número {numero} não é primo!')

if __name__ == '__main__':
    main()