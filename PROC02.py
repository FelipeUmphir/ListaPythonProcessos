import platform
import subprocess

def nome_so():
    system = platform.system()
    return system

def proc(processo):
    vetor_proc = []
    vetor_proc = processo.split(' ')
    subprocess.run(vetor_proc)

def main():
    opcao = 0
    so = nome_so()

    while (opcao != 9):
        print('\n1 - Listar processos')
        print('2 - Matar por PID')
        print('3 - Matar por nome')
        print('9 - Sair')

        opcao = int(input('Escolha: '))

        match opcao:

            case 1:
                if (so == 'Windows'):
                    processo = 'TASKLIST /FO TABLE'
                elif (so == 'Linux'):
                    processo = 'ps -ef'

                proc(processo)

            case 2:
                pid = input('Digite o PID: ')

                if (so == 'Windows'):
                    processo = 'TASKKILL /PID ' + pid
                elif (so == 'Linux'):
                    processo = 'kill -9 ' + pid

                proc(processo)

            case 3:
                nome_proc = input('Digite o nome do processo: ')

                if (so == 'Windows'):
                    processo = 'TASKKILL /IM ' + nome_proc
                elif (so == 'Linux'):
                    processo = 'pkill -f ' + nome_proc

                proc(processo)

            case 9:
                continue
            
            case _:
                print('Opção inválida')


if __name__ == '__main__':
    main()