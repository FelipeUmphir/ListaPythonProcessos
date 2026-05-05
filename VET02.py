def main():
    V = [0] * 100
    m = 0
    Ma = 0 
    Me = 0

    for i in range(100):
        V[i] = int(input('Digite um valor inteiro: '))

    for i in range(100):
        m = m + V[i]
        if V[i] > Ma:
            Ma = V[i]
        if V[i] < Me:
            Me = V[i]
        elif Me == 0:
            Me = V[i]

    media = m/100

    print(f'A média é: {media}')
    print(f'O maior valor é: {Ma} e o menor é: {Me}')

if __name__ == '__main__':
    main() 