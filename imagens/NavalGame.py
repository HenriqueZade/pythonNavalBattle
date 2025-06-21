from copy import deepcopy
import os
import random
import time

linhas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
colunas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

mapa_jogador1 = [['~'] * 15 for i in range(15)]
mapa_jogador2 = deepcopy(mapa_jogador1)  # copia o mapa do jogador 1
mapa_batalha1 = deepcopy(mapa_jogador1)
mapa_batalha2 = deepcopy(mapa_jogador1)

barco1 = 1
barco2 = 1

continuar = '0'
jogarContraIa = 0
jogadas_jogadores = 0
escolha = ''

contadorPosicao = 0
contador_jogador1 = 0
contador_jogador2 = 0

pontos1 = 0
pontos2 = 0

def resetarVariaveis():
    global linhas, colunas, mapa_jogador1, mapa_jogador2, barco1, barco2, continuar, jogarContraIa, jogarContraIa,\
    jogadas_jogadores, escolha, contadorPosicao, contador_jogador1, contador_jogador2, pontos1, pontos2, mapa_batalha1, mapa_batalha2

    mapa_jogador1 = [['~'] * 15 for i in range(15)]
    mapa_jogador2 = deepcopy(mapa_jogador1)  # copia o mapa do jogador 1
    mapa_batalha1 = deepcopy(mapa_jogador1)
    mapa_batalha2 = deepcopy(mapa_jogador1)

    barco1 = 1
    barco2 = 1

    continuar = 0
    jogarContraIa = 0
    jogadas_jogadores = 0
    escolha = ''

    contadorPosicao = 0
    contador_jogador1 = 0
    contador_jogador2 = 0

    pontos1 = 0
    pontos2 = 0

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(a):
    if a == 1:  # ver qual mapa vai ultilizar
        mapa = mapa_jogador1
    elif a == 2:
        mapa = mapa_jogador2
    elif a == 3:
        mapa = mapa_batalha1
    elif a == 4:
        mapa = mapa_batalha2

    print('/', end='  ┃  ')  # comeco

    for i in colunas:  # números em baixo
        if i >= 11:
            print(i, end='  ┃ ')
        elif i == 10:
            print(i, end=' ┃ ')
        else:
            print(i, end='  ┃  ')

    print()
    print('━' * 94)

    for index, value in enumerate(mapa):  # divido entre o index e valor naquele item do mapa
        print(linhas[index], end='  ┃  ')
        for j in value:
            print(j, end='  ┃  ')  # dois espaços, fica um melhor formatação
        print()
        print('━' * 94)

def barcos(modelo):
    if modelo == 1:
        barco = "n""n""n""n""n"  # encouraçado
        modelo = "encouraçado"
        return barco
    elif modelo == 2:
        barco = "n""n""n""n"  # porta-aviões
        modelo = "porta-aviões"
        return barco
    elif modelo == 3 or modelo == 4:
        barco = "n""n""n"  # contratorpedeiros
        modelo = "contratorpedeiro"
        return barco
    elif modelo == 5 or modelo == 6:
        barco = "n""n"  # submarino
        modelo = "submarino"
        return barco

def direcaoEscolhida():
    global direcao, coordenadaColuna, coordenadaLinha, linha, coluna
    try:
        direcao = int(input("\nEscolha se quer na horizontal(0) ou na vertical(1): "))
    except:
        direcaoEscolhida()
    if direcao > 1 or direcao < 0:
        direcaoEscolhida()

def linhaEscolhida():
    global direcao, coordenadaColuna, coordenadaLinha, linha, coluna, linhas
    coordenadaLinha = input("Escolha uma LINHA para posisionar os barcos utilizando as letra de A até O: ").lower()
    if coordenadaLinha in linhas:
        linha = ord(coordenadaLinha) - 97
    else: 
        linhaEscolhida()

def colunaEscolhida():
    global direcao, coordenadaColuna, coordenadaLinha, linha, coluna
    try:
        coordenadaColuna = int(input("Escolha uma COLUNA para posisionar os barcos utilizando números de 1 a 15: "))
        if coordenadaColuna > 0 and coordenadaColuna < 16:
            coluna = int(coordenadaColuna) - 1
        else:
            colunaEscolhida()
    except:
        colunaEscolhida()

def coordenadas():  # ver coordenadas

    if contador_jogador1 < 6 and contador_jogador2 < 6:
        direcaoEscolhida()
    linhaEscolhida()
    colunaEscolhida()

def funcaoPosicaoBarco1():
    global contadorPosicao, direcao
    if direcao == 0:
        for i in range(len(barco_modelo)):
            teste = (mapa_jogador1[linha][coluna + i] == '~')
            if teste == True:
                contadorPosicao += 1
    else:
        for i in range(len(barco_modelo)):
            teste = (mapa_jogador1[linha + 1][coluna] == '~')
            if teste == True:
                contadorPosicao += 1

def funcaoPosicaoBarco2():
    global contadorPosicao, direcao, barco_modelo
    if direcao == 0:
        for i in range(len(barco_modelo)):
            teste = (mapa_jogador2[linha][coluna + i] == '~')
            if teste == True:
                contadorPosicao += 1
    else:
        for i in range(len(barco_modelo)):
            teste = (mapa_jogador2[linha + 1][coluna] == '~')
            if teste == True:
                contadorPosicao += 1

def jogadas_ataque(num):
    if num % 2 == 0:
        jogador = 1
        return jogador
    elif num % 2 != 0:
        jogador = 2
        return jogador

def menu_inicial():
    global escolha
    global jogarContraIa
    print('\nBem vindo ao jogo Batalha Naval!\n'
          '\nEscolha uma opção dentro dessas:' 
          '\n1 - Jogar localmente com 2 Jogadores' 
          '\n2 - Jogar contra Ia' 
          '\n3 - Sair')

    while escolha not in ('1', '2', '3') or not len(escolha) == 1:
        escolha = input('\nSua escolha: ')

    escolha = int(escolha)
    if escolha == 2:
        jogarContraIa = 1
        limparTerminal()
        print('iniciando jogo contra Ia')
    else:
        limparTerminal()
        print('iniciando jogo localmente com 2 jogadores')

def randomIA():
    global direcao, linha, coluna
    direcao = random.randint(0,1)
    linha = random.randint(0,14)
    coluna = random.randint(0,14)

while continuar == '0':  # menu
    limparTerminal()
    resetarVariaveis()
    menu_inicial()

    while contador_jogador1 < 6 and contador_jogador2 < 6:  # colocar os navios

        print('\nVez do jogador 1\n')
        time.sleep(3)  # espera uns segundos pra começar
        limparTerminal()

        while contador_jogador1 < 6: # Vez do primeiro jogador colocar barcos

            barco_modelo = barcos(barco1)  # chama a função barcos para definir o tamanho do barco
            contadorPosicao = 0

            limparTerminal()
            print(f"Vocë tem {7 - barco1} barco(s) para jogar")
            print(f"Jogador 1 - Siga as instruções para colocar um barco de {len(barco_modelo)} casas\n")
            mostrar_mapa(1)

            coordenadas()  # ver coordenada

            limparTerminal()

            if direcao == 0:
                try:
                    funcaoPosicaoBarco1()
                    if contadorPosicao == len(barco_modelo):  # Tratamento de erro, para verificar se a coluna e a linha escolhida existem // e confirmar se tem espaço no local para colocar
                        mapa_jogador1[linha][coluna:(coluna + len(barco_modelo))] = barco_modelo
                        limparTerminal()
                        contador_jogador1 += 1
                        barco1 += 1
                    else:
                        print("Jogada Inválida ou Sem espaço para esse navio")
                        time.sleep(2)
                except:
                    print("Jogada Inválida ou Sem espaço para esse navio")
                    time.sleep(2)

            elif direcao == 1:
                try:
                    funcaoPosicaoBarco1()
                    if contadorPosicao == len(barco_modelo):  # Tratamento de erro, para verificar se a coluna e a linha escolhida existem // e confirmar se tem espaço no local para colocar
                        for index, value in enumerate(barco_modelo):
                            mapa_jogador1[linha + index][coluna] = value
                        limparTerminal()
                        contador_jogador1 += 1
                        barco1 += 1
                    else:
                        print("Jogada Inválida ou Sem espaço para esse navio")
                        time.sleep(2)
                except:
                    print("Jogada Inválida ou Sem espaço para esse navio")
                    time.sleep(2)

        limparTerminal()
        print('Seu mapa ficou assim!\n')
        mostrar_mapa(1)
        time.sleep(3)  # espera uns segundos pra começar

        if jogarContraIa == 0:
            print('\nPasse para o segundo jogador')
        else:
            print('\nPreparando mapa da IA')

        time.sleep(3)
        limparTerminal()

        while contador_jogador2 < 6: # Vez do jogador 2 colocar barcos

            barco_modelo = barcos(barco2)  # chama a função barcos para definir o tamanho do barco
            contadorPosicao = 0

            if jogarContraIa == 0:
                limparTerminal()
                print(f"Vocë tem {7 - barco2} barco(s) para jogar")
                print(f"Jogador 2 - Siga as instruções para colocar um barco de {len(barco_modelo)} casas\n")
                mostrar_mapa(2)

                coordenadas()  # ver coordenada

                limparTerminal()

            else: # IA
                randomIA()

            if direcao == 0:
                try:
                    funcaoPosicaoBarco2()

                    if contadorPosicao == len(barco_modelo):  # Tratamento de erro, para verificar se a coluna e a linha escolhida existem // e confirmar se tem espaço no local para colocar
                        mapa_jogador2[linha][coluna:(coluna + len(barco_modelo))] = barco_modelo
                        limparTerminal()
                        contador_jogador2 += 1
                        barco2 += 1
                    elif jogarContraIa == 0:
                        print("Jogada Inválida ou Sem espaço para esse navio")
                        time.sleep(2)
                except:
                    if jogarContraIa == 0:
                        print("Jogada Inválida ou Sem espaço para esse navio")
                        time.sleep(2)

            elif direcao == 1:
                try:
                    funcaoPosicaoBarco2()

                    if contadorPosicao == len(barco_modelo):  # Tratamento de erro, para verificar se a coluna e a linha escolhida existem // e confirmar se tem espaço no local para colocar
                        for index, value in enumerate(barco_modelo):
                            mapa_jogador2[linha + index][coluna] = value
                        limparTerminal()
                        contador_jogador2 += 1
                        barco2 += 1

                    elif jogarContraIa == 0:
                        print("Jogada Inválida ou Sem espaço para esse navio")
                        time.sleep(2)
                except:
                    if jogarContraIa == 0:
                        print("Jogada Inválida ou Sem espaço para esse navio")
                        time.sleep(2)

        if jogarContraIa == 0:
            limparTerminal()
            print('Seu mapa ficou assim!\n')
            mostrar_mapa(2) 
        else:
            limparTerminal()
            print('Mapa da Ia está pronto!')

        print('\nHora de ir pras rodadas de ataque!')
        time.sleep(5)


    while pontos1 < 19 and pontos2 < 19:
        jogador = jogadas_ataque(jogadas_jogadores) 
        
        if jogador == 1:
            limparTerminal()
            print('Jogador 1 - Faça o seu ataque!\n')
            mostrar_mapa(3)

            print()
            coordenadas()
            while mapa_batalha1[linha][coluna] == 'O':
                    coordenadas()  # ver coordenada

            limparTerminal()

            if mapa_jogador2[linha][coluna] == '~':  # Tratamento de erro, para verificar se a coluna e a linha escolhida existem // e confirmar se tem espaço no local para colocar
                mapa_batalha1[linha][coluna] = 'O'
                print('Você errou!\n')

            elif mapa_jogador2[linha][coluna] == 'N':
                mapa_batalha1[linha][coluna] = 'X'
                pontos1 += 1
                print('Você acertou!\n')
            time.sleep(2)
            jogadas_jogadores += 1
            mostrar_mapa(3)
            time.sleep(5)

        if jogador == 2:
            limparTerminal()
            if jogarContraIa == 0:
                print('Jogador 2 - Faça o seu ataque!\n')
                mostrar_mapa(4)

                print()
                coordenadas()  # ver coordenada

                while mapa_batalha2[linha][coluna] == 'O':
                        coordenadas()

                limparTerminal()

            elif jogarContraIa == 1: # nao deixar a ia jogar em lugar que ja tem O
                randomIA()
                while mapa_batalha2[linha][coluna] == 'O':
                        randomIA()

            if mapa_jogador1[linha][coluna] == '~':  # Tratamento de erro, para verificar se a coluna e a linha escolhida existem // e confirmar se tem espaço no local para colocar
                mapa_batalha2[linha][coluna] = 'O'
                if jogarContraIa == 0:
                    print('Você errou!\n')
                else:
                    print('Computador errou!\n')
            elif mapa_jogador1[linha][coluna] == 'N':
                mapa_batalha2[linha][coluna] = 'X'
                pontos2 += 1
                if jogarContraIa == 0:
                    print('Você acertou!\n')
                else:
                    print('Computador acertou!\n')

            time.sleep(2)
            jogadas_jogadores += 1
            mostrar_mapa(4)
            time.sleep(5)

        limparTerminal()
        print(f'Jogador 1 tem {pontos1} ponto(s)!')
        if jogarContraIa == 1:
            print(f'Computador tem {pontos2} ponto(s)!')
        else:
            print(f'Jogador 2 tem {pontos2} ponto(s)!')

    continuar = input('Você quer continuar sim(0) não(1)?: ')
    while continuar != '0' and continuar != '1':
        continuar = input('Você quer continuar sim(0) não(1)?: ')

print('\nFim!')
