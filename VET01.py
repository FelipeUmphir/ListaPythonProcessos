def main():
    V = [0] * 50
    soma = 0
    ac = 0
    c = 0

    for i in range(50):
        V[i] = int(input('Digite um valor inteiro: '))

    for i in range(50):
        if 10 < V[i] < 200:
            ac = ac + V[i]
            c = c + 1
        if (V[i] % 2) != 0:
            soma = soma + V[i]

    media = ac / c

    print(f'A média é: {media}')
    print(f'A soma dos ímpares é: {soma}')

if __name__ == '__main__':
    main() 