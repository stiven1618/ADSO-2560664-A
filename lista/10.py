#hecho por joel oliveros
import random
tam=round(random.randint(5,10))
vec=[]
dif=[]
media=0
print("tam=",tam)
for i  in range (tam):
    vec.append(round(random.random()*100))
print("lista", vec)
for i in vec:
    media+=i
media=media/len(vec)
print("pro,ds",media)
suma=0
for i in range(len(vec)):
    x=(vec[i]-media)**2
    dif.append(x)
    suma+=x
print("suma",suma)
print("dest estandar",(suma/len(vec))**0.5)
