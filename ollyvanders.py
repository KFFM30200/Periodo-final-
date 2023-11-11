Clientes = 0 
Compraron = 0
Nocompraron = 0
Varitasven = {"Varita de Saúco": 0, "Varita de Espino": 0, "Varita de sauce": 0, "Varita de acebo": 0}

while True:
    print(" ")
    In = input("¿Entra un cliente? (si/no):").lower()
  
    if In != 'si':
        break
    Clientes+=1

    compro_algo = input("¿Compro algo? (si/no) :").lower()
  
    if compro_algo == 'si':
      Compraron +=1
      print(" ")
      print("Escoja su varita:")
      print(" ")
      print("1) Varita de Saúco")
      print("2) Varita de Espino")
      print("3) Varita de sauce")
      print("4) Varita de acebo")
      varita_com = input("¿Que varita compró? Escoje(1, 2, 3, 4) : ")
  
    if varita_com in ['1','2', '3', '4']:
      varita_escojida = {'1': 'Varita de Saúco','2': 'Varita de Espino','3': 'Varita de sauce','4':'Varita de acebo'}[varita_com]
      Varitasven[varita_escojida]+=1
    else:
      print("Opción no valida")
else:
  Nocompraron +=1

print(" ")
print(f"Clientes totales: {Clientes}")
print(f"Clientes que compraron: {Compraron}")
print(f"Clientes que no compraron: {Nocompraron}")
print(" ")
print("Hoy vendieron")
print(f"{Varitasven['Varita de Saúco']} varita de sauco")
print(f"{Varitasven['Varita de Espino']} varita de Espino")
print(f"{Varitasven['Varita de sauce']}varita de sauce")
print(f"{Varitasven['Varita de acebo']} varita de acebo")
print(" ")
print("Qué gran día para Ollivanders!") 
