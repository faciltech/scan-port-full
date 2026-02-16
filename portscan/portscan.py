#!/usr/bin/env python3
# ==============================================================
#  Autor       : Eduardo Amaral
#  Email       : eduardo4maral@protonmail.com
#  YouTube     : https://www.youtube.com/faciltech
#  GitHub      : https://github.com/faciltech
#  Site        : https://www.eduardo-amaral.com
#  LinkedIn    : https://www.linkedin.com/in/eduardo4maral/
#  Atualização : 16/02/2026
# ==============================================================

import socket
import sys
from datetime import datetime


# ==================== IDENTIDADE VISUAL ====================

BANNER = r"""
  ███████╗ ██████╗ █████╗ ███╗   ██╗      ██████╗  ██████╗ ██████╗ ████████╗
  ██╔════╝██╔════╝██╔══██╗████╗  ██║      ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
  ███████╗██║     ███████║██╔██╗ ██║█████╗██████╔╝██║   ██║██████╔╝   ██║   
  ╚════██║██║     ██╔══██║██║╚██╗██║╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║   
  ███████║╚██████╗██║  ██║██║ ╚████║      ██║     ╚██████╔╝██║  ██║   ██║   
  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

                 SCAN-PORT - PROFESSIONAL EDITION
"""


class Cores:
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AZUL = "\033[94m"
    AMARELO = "\033[93m"
    RESET = "\033[0m"


TIMEOUT = 0.5


# ==================== FUNÇÕES ====================

def mostrar_banner():
    print(Cores.AMARELO + BANNER + Cores.RESET)
    print("Autor       : Eduardo Amaral")
    print("Email       : eduardo4maral@protonmail.com")
    print("YouTube     : https://www.youtube.com/faciltech")
    print("GitHub      : https://github.com/faciltech")
    print("Site        : https://www.eduardo-amaral.com")
    print("LinkedIn    : https://www.linkedin.com/in/eduardo4maral/")
    print("Atualização : 16/02/2026")
    print("=" * 65)
    print(f"{Cores.AMARELO}[amaralSecTools]{Cores.RESET} SCAN-PORT v1.0")
    print("=" * 65)


def resolver_alvo(alvo):
    try:
        return socket.gethostbyname(alvo)
    except socket.gaierror:
        return None


def escolher_lista_portas():

    portas_top10 = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445]
    portas_top20 = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143,
                    443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    portas_top50 = list(set(portas_top20 + [
        5060, 5666, 6001, 8000, 8443, 8888,
        10000, 32768, 49152, 49154
    ]))
    portas_total = range(1, 65536)

    print("\nEscolha o tipo de varredura:")
    print("1 - Top 10 portas")
    print("2 - Top 20 portas")
    print("3 - Top 50 portas")
    print("4 - Todas as 65535 portas")
    print("0 - Porta específica")

    opcao = input(">>> ").strip()

    if opcao == "1":
        return portas_top10
    elif opcao == "2":
        return portas_top20
    elif opcao == "3":
        return portas_top50
    elif opcao == "4":
        return portas_total
    elif opcao == "0":
        try:
            porta = int(input("Digite a porta: "))
            if 1 <= porta <= 65535:
                return [porta]
        except:
            pass

    print(Cores.VERMELHO + "Opção inválida!" + Cores.RESET)
    return escolher_lista_portas()


def port_scan(ip, alvo):

    lista_portas = escolher_lista_portas()

    print(f"\n{Cores.AZUL}Iniciando scan em:{Cores.RESET} {alvo} ({ip})")
    inicio = datetime.now()

    portas_abertas = []

    for porta in lista_portas:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(TIMEOUT)
                if s.connect_ex((ip, porta)) == 0:
                    print(f"{Cores.VERDE}[ABERTA]{Cores.RESET} Porta {porta}")
                    portas_abertas.append(porta)
        except KeyboardInterrupt:
            print("\nScan interrompido.")
            sys.exit()

    fim = datetime.now()

    print("\n" + "=" * 65)
    print(Cores.AMARELO + "Resultado do Scan" + Cores.RESET)
    print("=" * 65)
    print(f"Portas abertas: {len(portas_abertas)}")
    if portas_abertas:
        print("Lista:", portas_abertas)
    print(f"Tempo total: {fim - inicio}")


def menu_pos_scan():
    print("\nO que deseja fazer agora?")
    print("1 - Novo tipo de varredura (mesmo alvo)")
    print("2 - Novo alvo")
    print("0 - Sair")

    return input(">>> ").strip()


# ==================== MAIN ====================

def main():

    mostrar_banner()

    while True:

        alvo = input("\nDigite o IP ou domínio alvo: ").strip()
        ip = resolver_alvo(alvo)

        if not ip:
            print(Cores.VERMELHO + "Alvo inválido!" + Cores.RESET)
            continue

        while True:

            port_scan(ip, alvo)

            escolha = menu_pos_scan()

            if escolha == "1":
                continue
            elif escolha == "2":
                break
            elif escolha == "0":
                print(Cores.AMARELO + "\nEncerrando SCAN-PORT..." + Cores.RESET)
                sys.exit()
            else:
                print(Cores.VERMELHO + "Opção inválida!" + Cores.RESET)


if __name__ == "__main__":
    main()
