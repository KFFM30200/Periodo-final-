lecturas = int(input("¿Cuantas temperaturas tienes?"))
contador = 0
temperatura = 0
erroneas = 0
correctas = 0

while contador < lecturas:
  contador +=1
  temperatura = float(input("Inserta la temperatura"))
if temperatura >= 10 and temperatura <= 40:
  pass
else: 
  erroneas +=1
print(erroneas)
porcentaje = (erroneas * 100)/ lecturas
print(porcentaje)
