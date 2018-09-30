import random

def tela_escolha():
    print("**********************************")
    print("******** WARRIORS BATTLE *********")
    print("**********************************")
    print("****** Choose your Warrior *******")
    print("1 - {} ".format(warrior_list[0]))
    print("2 - {} ".format(warrior_list[1]))
    print("3 - {} ".format(warrior_list[2]))
    print("4 - {} ".format(warrior_list[3]))
    print("5 - {} ".format(warrior_list[4]))
    print("6 - {} ".format(warrior_list[5]))


warrior_list = ["Samurai", "Ninja", "Viking", "Assassino", "Templário", "Arqueiro"]
lista_habilidades = ["Inteligência", "Velocidade", "Agilidade", "Força"]
life_player_one = 100
life_player_two = 100
rodada = 1


tela_escolha()

escolha_player_one = int(input("Qual o seu guerreiro? "))

player_one = escolha_player_one
warrior_player_one = warrior_list[player_one -1]
print("Você escolheu {} como seu guerreiro".format(warrior_player_one))
warrior_list.remove(warrior_player_one)

escolha_player_two = random.SystemRandom()
warrior_player_two = escolha_player_two.choice(warrior_list)
print("Eu escolho {} como meu guerreiro".format(warrior_player_two))


print("{} vs {} ".format(warrior_player_one, warrior_player_two))



while (life_player_one > 0):
    print("======================= ")
    print("====== Rodada {} ====== ".format(rodada))
    print("======================= ")
    print(lista_habilidades)
    escolha_habilidade = int(input("====== Escolha a habilidade ====== \n"))
    habilidade_escolhida = lista_habilidades[escolha_habilidade - 1]
    print(habilidade_escolhida)
    damage = 5
    life_player_one = life_player_one - damage
    print(life_player_one)
    #life_player_two = 100 - 4

    rodada += 1
#rodada = 1

#for rodada in range (1, ):