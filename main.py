import random

jogador1=()
jogador2=()
maquina1=()
maquina2=()
escolha=()
continuar=1

while continuar==1:
    print("digite 1 para jogador contra maquina")
    print("digite 2 para jogador contra jogador")
    print("digite 3 para maquina contra maquina")
    escolha=float(input("Qual sua escolha?"))
    if escolha == 1:
        print("digite 1 para pedra")
        print("digite 2 para tesoura")
        print("digite 3 para papel")
        jogador1 = float(input("Qual sua jogada?"))
        maquina1 = random.randrange(1,3)
        if jogador1==1:
            if maquina1==1:
                print("Deu empate.")
            else:
                if maquina1==2:
                    print("Parabéns, você ganhou!!!")
                else:
                    print("Que pena, você perdeu.")
        if jogador1==2:
            if maquina1==1:
                print("Que pena, você perdeu.")
            else:
                 if maquina1==2:
                     print("Deu empate.")
                 else:
                     print("Que pena, você perdeu.")
        if jogador1==3:
            if maquina1==1:
                print("Parabéns, você venceu!!!")
            else:
                if maquina1==2:
                    print("Que pena, você perdeu.")
                else:
                    print("Deu empate.")
    if escolha == 2:
        print("digite 1 para pedra")
        print("digite 2 para tesoura")
        print("digite 3 para papel")
        jogador1 = float(input("Jogador 1, qual a sua jogada?"))
        jogador2 = float(input("Jogador 2, qual a sua jogada?"))
        if jogador1 == 1:
            if jogador2 == 1:
                print("Deu empate.")
            else:
                if jogador2 == 2:
                    print("Jogador 1 venceu!!!")