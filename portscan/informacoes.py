#!/usr/bin/env python3

import sys

PORTAS = {
    "1": sorted({21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389}),
    "2": sorted({
        21, 22, 23, 25, 53, 80, 110, 135, 139, 143,
        443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080
    }),
    "3": sorted({
        21, 22, 23, 25, 53, 80, 110, 135, 139, 143,
        443, 445, 993, 995, 1723, 3306, 3389, 5060,
        5666, 5900, 6001, 8000, 8080, 8443, 8888,
        10000, 32768, 49152, 49154
    }),
    "4": range(1, 65536)
}


def mostrar_banner():
    print(BANNER)
    print(AUTHOR)
    print("-" * 55)


def escolher_lista_portas():
    print("Selecione uma lista de Portas:")
    print("0 - Uma porta específica")
    print("1 - Lista Top 10")
    print("2 - Lista Top 20")
    print("3 - Lista Top 50")
    print("4 - Verificar todas as 65535 portas (pode demorar)")

    escolha = input("\n>>> ").strip()

    if escolha == "0":
        return escolher_porta_unica()

    if escolha in PORTAS:
        return PORTAS[escolha]

    print("Opção inválida!")
    sys.exit(1)


def escolher_porta_unica():
    try:
        porta = int(input("Digite a porta (1-65535): "))
        if 1 <= porta <= 65535:
            return [porta]
        else:
            raise ValueError
    except ValueError:
        print("Porta inválida! Digite um número entre 1 e 65535.")
        sys.exit(1)


def mostrar_linha():
    print("-" * 55)


if __name__ == "__main__":
    mostrar_banner()
    portas = escolher_lista_portas()
    mostrar_linha()
    print(f"Total de portas selecionadas: {len(portas)}")
    print(portas)
