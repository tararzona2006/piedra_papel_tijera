import random

#input

bot= random.randint(1,3)
juagador=int(input("ingrese tu obcion, 1=piedra-2=papel-3=tijera: "))

#processing

if bot==1 and juagador==3:
    print("bot gana: piedra le gana a tijeras")
elif bot==2 and juagador==1:
    print("bot gana: papel le gana a piedra")
elif bot==3 and juagador==2:
    print("bot gana: tijeras le gana a papel")
elif juagador==1 and bot==3:
    print("jugador gana: piedra le gana a tijeras")
elif juagador==2 and bot==1:
    print("jugador gana: papel le gana a piedra")
elif juagador==3 and bot==2:
    print("jugador gana: tijeras le gana a papel")
elif juagador==bot:
    print("EmPaTe")
elif juagador>3:
    print("OBCION NO VALIDA")

