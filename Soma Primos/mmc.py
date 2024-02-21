def primos_ate(limite):
    n_primos = []
    for n in range(2, limite + 1):
        if n > 2 and n % 2 == 0:
            continue
        if is_primo(n):
            n_primos.append(n)
    return n_primos
    
def mmc(*args):
    primos = primos_ate(max(args))
    args = list(args)
    i = 0
    fatores = []

    while not is_one(args):
        div = False
        for a, n in enumerate(args):
            if n % primos[i] == 0:
                args[a] = n // primos[i]
                div = True
        if div:
            fatores.append(primos[i])    
        elif i < len(primos) -1:
            i += 1

    mmc = 1
    for f in fatores:
        mmc *= f
    return mmc

def mdc(*args):
    primos = primos_ate(max(args))
    args = list(args)
    i = 0
    fatores_comuns = []

    while not is_one(args):
        div = True
        for a, n in enumerate(args):
            if n % primos[i] == 0:
                args[a] = n // primos[i]
            else:
                div = False
        if div:
            fatores_comuns.append(primos[i])    
        elif i < len(primos) -1:
            i += 1

    mdc = 1
    for f in fatores_comuns:
        mdc *= f
    return mdc

def is_one(lista) -> bool:
    for e in lista:
        if e != 1:
            return False
    return True

def is_primo(num) -> bool:
    divisor = 2
    while True:
        if divisor >= num % divisor and  num % divisor != 0 or num == divisor:
            return True

        if num % divisor == 0:
            return False 

        divisor += 1
