# salir = False
# while not salir:
#     entrada=input(">")
#     if entrada == "adios":
#         salir = True
#     else:
#         print("Entrada")
frutas = {"Fresa":2000,
          "Mango":1000,
          "Mandarina":5000
          }
for fruta , precio in frutas.items():
    print(f"{fruta}:{precio}")