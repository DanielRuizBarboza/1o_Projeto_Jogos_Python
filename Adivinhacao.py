import random


def jogar():
    pontos = 1000

    imprime_msg_inicial()
    numero_secreto = gera_numero_secreto()
    nivel = seleciona_nivel_dificuldade()
    total_de_tentativas = escolha_dificuldade(nivel)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = recebe_chute()

        print("Você chutou: ", chute)
        if chute < 1 or chute > 100:
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            imprime_msg_vencedora(pontos, total_de_tentativas, nivel, rodada)
            break
        elif rodada < total_de_tentativas:
            if (maior):
                imprime_msg_maior()
            elif (menor):
                imprime_msg_menor()

            pontos = calcula_pontos(pontos, chute, numero_secreto)
        else:
            fim_de_jogo(numero_secreto)

    else:
        print("Fim do Jogo.")


def imprime_msg_inicial():
    print("""
    *********************************
    Bem vindo ao jogo de adivinhação!
    *********************************
        """)


def gera_numero_secreto():
    return random.randrange(1, 101)


def seleciona_nivel_dificuldade():
    print("Escolha o nível de dificuldade: ")
    print(" (1) - Fácil \n (2) - Médio \n (3) - Difícil\n")
    return int(input("Defina o nível: "))


def escolha_dificuldade(nivel):
    if (nivel == 1):
        return 20
    elif (nivel == 2):
        return 10
    else:
        return 5


def recebe_chute():
    return int(input("Digite o seu chute entre 1 e 100: "))


def imprime_msg_vencedora(pontos, total_de_tentativas, nivel, rodada):
    print("Você acertou! Parabéns!")
    pontos = pontos + ((total_de_tentativas * nivel) - rodada) * (nivel * nivel)
    print("Sua pontuação foi de: {} pontos".format(pontos))


def imprime_msg_maior():
    print("Você errou, seu chute foi maior que o valor secreto.\n"
          "Tente outra vez!")


def imprime_msg_menor():
    print("Você errou, seu chute foi menor que o valor secreto.\n"
          "Tente outra vez!")


def calcula_pontos(pontos, chute, numero_secreto):
    pontos_perdidos = abs(chute - numero_secreto) * 10
    return pontos - pontos_perdidos


def fim_de_jogo(numero_secreto):
    print("Você errou e suas tentativas acabaram! :(")
    print("O numero secreto era:", numero_secreto)


if __name__ == "__main__":
    jogar()
