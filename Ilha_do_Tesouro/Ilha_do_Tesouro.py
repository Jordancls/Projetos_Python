print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem -vindo a Ilha do Tesouro.")
print("A Nossa missão é encontrar o tesouro.")

#Escreva seu código abaixo desta linha 👇

choice1 = input('Você\'está em uma estrada Cruzada.Onde você quer ir? Digite "esquerda" ou "direita" \n').lower()
if choice1 == "esquerda":
  choice2 = input('Você\'veio a um lago. Há uma ilha no meio do lago.Digite "espere" para esperar por um barco.Digite "nadar" para nadar. \n').lower()
  if choice2 == "espere":
    choice3 = input("Você chega à ilha ileso.Há uma casa com 3 portas.Um vermelho, um amarelo e outro azul.Qual cor você escolhe? \n").lower()
    if choice3 == "vermelho":
      print("É uma sala cheia de fogo.Fim de jogo.")
    elif choice3 == "amarelo":
      print("Você encontrou o tesouro!Você ganhou!")
    elif choice3 == "azul":
      print("Você entrou em uma sala de animais.Fim de jogo.")
    else:
      print("Você escolheu uma porta que não existe.Fim de jogo.")
  else:
    print("Você é atacado por uma truta irritada.Fim de jogo.")
else:
  print("Você caiu em um buraco.Fim de jogo.")