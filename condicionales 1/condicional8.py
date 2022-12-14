minutos = float(input("Escriba cuantos minutos duro la llamada: "))

if(minutos <= 3):
    print("La llamada tiene un costo de",minutos * 200)
elif(minutos >=4):
    print("La llamada tiene un costo de",450 + minutos * 50)