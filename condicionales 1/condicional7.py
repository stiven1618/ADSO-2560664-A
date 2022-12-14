h = float(input("Escriba el numero de horas que trabajo : "))
he = float(input("Escriba cuantas horas horas extra trabajo : "))

salario = (h * 2600)
salarioextra = (40 * 2600 + he * 5000)

if(h <= 40):
    print(salario)
elif(h >= 41):
    print(salarioextra)




