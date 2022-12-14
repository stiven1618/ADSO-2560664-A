#hecho por angelo
import random
tam=1
list=[]
while tam<10 or tam>25:
    tam=int(round(random.random()*100))
print(tam)
for i in range (tam):
    list.append(round(random.random()*100))
print (list)
primos=[]
for i in range (len(list)):
    if list[1]%2==0:
        primos.append(list[i])
print("los primos son:", primos,"y el total son",len(primos))
