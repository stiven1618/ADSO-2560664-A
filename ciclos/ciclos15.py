x = int(input("Digite un numero positivo: "))

for i in range(x):
    for j in range(1,x+1):
        print(j," ",end="")
    x = x-1
    print("")