Alexa = input("Escribe algo")
Separar = Alexa.split()
Veces = Separar.count("Alexa")
print(Veces)
if Veces == 1:
  print("¿Dime, cómo puedo ayudarte?")
elif Veces >1:
  print("Tranquilo, solo di mi nombre una vez")
