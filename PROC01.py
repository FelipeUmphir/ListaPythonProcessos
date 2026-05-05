import platform
import subprocess

def nome_so():
    system = platform.system()
    return system

def le_processo(processo, os):
    vetor_proc = []
    vetor_proc = processo.split(' ')

    saida = subprocess.Popen(vetor_proc, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors='ignore')

    while (linha != ''):
        if (os == 'Windows'):
            if ('Média' in linha):
                partes = linha.split(',')
                for parte in partes:
                    if ('Média' in parte):
                        valor = parte.split('=')[1].strip()
                        print('Média =', valor)

        elif (os == 'Linux'):
            if ('rtt' in linha):
                partes = linha.split('=')
                valores = partes[1].strip().split('/')
                avg = valores[1]
                print('Average =', avg, 'ms')

        linha = saida.stdout.readline().decode('utf-8', errors='ignore')

def main():
    so = nome_so()

    if (so == 'Linux'):
        processo = 'ping -4 -c 10 www.google.com.br'
    elif (so == 'Windows'):
        processo = 'ping -4 -n 10 www.google.com.br'

    le_processo(processo, so)

if __name__ == '__main__':
    main()