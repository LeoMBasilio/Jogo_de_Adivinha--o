import os
from random import randint
import time

'''
     _       _ _       _       _                /\/|       
    / \   __| (_)_   _(_)_ __ | |__   __ _  ___|/\/_  ___  
   / _ \ / _` | \ \ / / | '_ \| '_ \ / _` |/ __/ _` |/ _ \ 
  / ___ \ (_| | |\ V /| | | | | | | | (_| | (_| (_| | (_) |
 /_/   \_\__,_|_| \_/ |_|_| |_|_| |_|\__,_|\___\__,_|\___/ 
                                            )_)            

    by leonardo
'''

def RandomNumber():
    return randint(0, 100)

def StartGame(number, chance):
    choice = int(input("Adivinhe o numero entre 1 e 100: "))
    while chance > 0:
        if choice == number:
            return True
        elif choice > number:
            print("#######################################")
            print("## o numero a ser adivinhado e menor ##")
            print("#######################################")
        else:
            print("#######################################")
            print("## o numero a ser adivinhado e maior ##")
            print("#######################################")
        
        choice = int(input("Nova tentativa: "))

        chance-=1

    if chance==0:
        return False

def DificultSelector():
    print("Selecione a dificuldade: ")
    print("1. Fácil (20 tentativas)")
    print("2. Médio (10 tentativas)")
    print("3. Difícil (5 tentativas)")

    while True:
        choice = input("Escolha uma opção: ")
        if choice == "1":
            return 20
        elif choice == "2":
            return 10
        elif choice == "3":
            return 5
        else:
            print("Opção inválida. Tente novamente.")

def Menu():
    while True:
        print("*********************************")
        print("** BEM VINDO AO JOGO DE ADIVINHAÇÃO **")
        print("*********************************")
        print("1. Iniciar")
        print("0. Sair")
        
        choice = int(input("Escolha uma opção: "))

        if choice != 0:
            dificult = DificultSelector()

        match choice:
            case 1:
                if StartGame(RandomNumber(), dificult):
                    print("############################################################")
                    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗")
                    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║")
                    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║")
                    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║")
                    print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║")
                    print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝")
                    print("############################################################")
                else:
                    print("##########################################################################")
                    print(" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
                    print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
                    print("██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
                    print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
                    print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
                    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
                    print("##########################################################################")

                time.sleep(10)

                os.system("cls")
            case 0:
                exit()

if __name__ == "__main__":
    Menu()