import os
import random
from colorama import Fore, Style

def validar_arquivo(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        print(f"{Fore.RED}O arquivo de senhas não foi encontrado.{Style.RESET_ALL}")
        return False
    return True

def filtrar_senhas_4_digitos():
    caminho_arquivo = os.path.expanduser("/senhas.txt")
    caminho_saida = os.path.expanduser("/senhas_filtradas_4.txt")

    if not validar_arquivo(caminho_arquivo):
        return

    senhas_filtradas = []
    senhas_unicas = set()

    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            senha = linha.strip()
            if len(senha) == 4 and senha.isalnum() and senha not in senhas_unicas:
                senhas_filtradas.append(senha)
                senhas_unicas.add(senha)

    with open(caminho_saida, "w") as arquivo_saida:
        for senha in senhas_filtradas:
            arquivo_saida.write(senha + "\n")

    print(f"{Fore.GREEN}Senhas filtradas foram salvas no arquivo {caminho_saida}.{Style.RESET_ALL}")

def filtrar_senhas_8_digitos():
    caminho_arquivo = os.path.expanduser("/senhas.txt")
    caminho_saida = os.path.expanduser("/senhas_filtradas_8.txt")

    if not validar_arquivo(caminho_arquivo):
        return

    senhas_filtradas = []
    senhas_unicas = set()

    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            senha = linha.strip()
            if len(senha) == 8 and senha.isalnum() and senha not in senhas_unicas:
                senhas_filtradas.append(senha)
                senhas_unicas.add(senha)

    with open(caminho_saida, "w") as arquivo_saida:
        for senha in senhas_filtradas:
            arquivo_saida.write(senha + "\n")

    print(f"{Fore.GREEN}Senhas filtradas foram salvas no arquivo {caminho_saida}.{Style.RESET_ALL}")

def filtrar_senhas_10_digitos():
    caminho_arquivo = os.path.expanduser("/senhas.txt")
    caminho_saida = os.path.expanduser("/senhas_filtradas_10.txt")

    if not validar_arquivo(caminho_arquivo):
        return

    senhas_filtradas = []
    senhas_unicas = set()

    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            senha = linha.strip()
            if len(senha) == 10 and senha.isalnum() and senha not in senhas_unicas:
                senhas_filtradas.append(senha)
                senhas_unicas.add(senha)

    with open(caminho_saida, "w") as arquivo_saida:
        for senha in senhas_filtradas:
            arquivo_saida.write(senha + "\n")

    print(f"{Fore.GREEN}Senhas filtradas foram salvas no arquivo {caminho_saida}.{Style.RESET_ALL}")

def filtrar_senhas_12_digitos():
    caminho_arquivo = os.path.expanduser("/senhas.txt")
    caminho_saida = os.path.expanduser("/senhas_filtradas_12.txt")

    if not validar_arquivo(caminho_arquivo):
        return

    senhas_filtradas = []
    senhas_unicas = set()

    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            senha = linha.strip()
            if len(senha) == 12 and senha.isalnum() and senha not in senhas_unicas:
                senhas_filtradas.append(senha)
                senhas_unicas.add(senha)

    with open(caminho_saida, "w") as arquivo_saida:
        for senha in senhas_filtradas:
            arquivo_saida.write(senha + "\n")

    print(f"{Fore.GREEN}Senhas filtradas foram salvas no arquivo {caminho_saida}.{Style.RESET_ALL}")

def gerar_senhas_aleatorias(comprimento, caracteres_especiais=False, numeros=False, letras_maiusculas=False, letras_minusculas=False, quantidade=1):
    caracteres_permitidos = ""
    if caracteres_especiais:
        caracteres_permitidos += "!@#$%^&*()_-+=<>?/\\"
    if numeros:
        caracteres_permitidos += "0123456789"
    if letras_maiusculas:
        caracteres_permitidos += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letras_minusculas:
        caracteres_permitidos += "abcdefghijklmnopqrstuvwxyz"

    senhas_geradas = []

    for _ in range(quantidade):
        senha = ''.join(random.choice(caracteres_permitidos) for _ in range(comprimento))
        senhas_geradas.append(senha)

    caminho_saida = os.path.expanduser("/senhas_geradas.txt")

    with open(caminho_saida, "w") as arquivo_saida:
        for senha in senhas_geradas:
            arquivo_saida.write(senha + "\n")

    print(f"{Fore.GREEN}Senhas aleatórias geradas foram salvas no arquivo {caminho_saida}.{Style.RESET_ALL}")

def verificar_forca_senha(senha):
    forca = 0

    # Critério de comprimento mínimo
    if len(senha) >= 8:
        forca += 1

    # Critério de uso de caracteres especiais
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>/?\\|`~" for char in senha):
        forca += 1

    # Critério de uso de letras maiúsculas e minúsculas
    if any(char.isupper() for char in senha) and any(char.islower() for char in senha):
        forca += 1

    # Critério de uso de números
    if any(char.isdigit() for char in senha):
        forca += 1

    return forca

def exibir_menu():
    while True:
        print(f"{Fore.YELLOW}==== MENU ===={Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Filtrar senhas de 4 dígitos{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Filtrar senhas de 8 dígitos{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Filtrar senhas de 10 dígitos{Style.RESET_ALL}")
        print(f"{Fore.CYAN}4. Filtrar senhas de 12 dígitos{Style.RESET_ALL}")
        print(f"{Fore.CYAN}5. Gerar senhas aleatórias{Style.RESET_ALL}")
        print(f"{Fore.CYAN}6. Verificar força da senha{Style.RESET_ALL}")
        print(f"{Fore.RED}0. Sair{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Script made by @MrRenan777{Style.RESET_ALL}")

        opcao = input(f"{Fore.YELLOW}Escolha uma opção: {Style.RESET_ALL}")

        if opcao == "1":
            filtrar_senhas_4_digitos()
        elif opcao == "2":
            filtrar_senhas_8_digitos()
        elif opcao == "3":
            filtrar_senhas_10_digitos()
        elif opcao == "4":
            filtrar_senhas_12_digitos()
        elif opcao == "5":
            comprimento = int(input(f"{Fore.YELLOW}Informe o comprimento da senha: {Style.RESET_ALL}"))
            caracteres_especiais = input(f"{Fore.YELLOW}Incluir caracteres especiais? (S/N): {Style.RESET_ALL}").lower() == "s"
            numeros = input(f"{Fore.YELLOW}Incluir números? (S/N): {Style.RESET_ALL}").lower() == "s"
            letras_maiusculas = input(f"{Fore.YELLOW}Incluir letras maiúsculas? (S/N): {Style.RESET_ALL}").lower() == "s"
            letras_minusculas = input(f"{Fore.YELLOW}Incluir letras minúsculas? (S/N): {Style.RESET_ALL}").lower() == "s"
            quantidade = int(input(f"{Fore.YELLOW}Quantidade de senhas a serem geradas: {Style.RESET_ALL}"))
            gerar_senhas_aleatorias(comprimento, caracteres_especiais, numeros, letras_maiusculas, letras_minusculas, quantidade)
        elif opcao == "6":
            senha = input(f"{Fore.YELLOW}Digite uma senha para verificar a força: {Style.RESET_ALL}")
            forca = verificar_forca_senha(senha)
            print(f"Força da senha: {forca}/4")
        elif opcao == "0":
            print(f"{Fore.RED}Saindo do programa...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")

# Executar o programa
exibir_menu()
