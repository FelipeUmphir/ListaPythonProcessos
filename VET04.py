def main():
    V = [0] * 30
    Vp = [0] * 30
    c = 0
    m = 0
    quant = 0

    for i in range(30):
        V[i] = float(input('Digite um valor inteiro: '))

    for i in range(30):
        m = m + V[i]

    media = m / 30

    for i in range(30):
        if V[i] > media:
            quant = quant + 1
        if V[i] < media:
            Vp[c] = i
            c = c + 1

    print(f'A média é: {media}')
    print(f'A quantidade de notas acima da média é: {quant}')
    print(f'Os índices dos valores abaixo da média é: {Vp[:c]}')

if __name__ == '__main__':
    main() 