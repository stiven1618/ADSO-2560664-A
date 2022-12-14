
def  iguales(n1,n2,n3):

    if (n1 == n2 == n3):
        return("los 3 numeros son iguales")
    elif (n1 == n2 != n3):
        return("los dos numeros son iguales")
    elif (n3 == n2 != n1):
        return("los dos numeros son iguales")
    elif (n3 == n1 != n2):
        return("los dos numeros son iguales")
    else:
        return("los numero no son iguales")
    
n1 = float(input("introduzca un numero: "))
n2 = float(input("introduzca un numero: "))
n3 = float(input("introduzca un numero: "))
print (iguales(n1,n2,n3))