num = int(input("Ingresa un número : "))
if num>0:
    print ("los divisores son : ")
    for i in range (1,num+1,1):
        if num%i==0:
            print (i)
elif num<0:
    print ("los divisores son : ")
    for i in range (-1,num-1,-1):
        if num%i==0:
            print (i)
else:
    print ("ningun numero es divisible por 0")