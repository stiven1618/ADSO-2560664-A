#hecho por angelo
import random
vector=[round(random.random()*10)for i in range(10)]
print("lista",vector)
hola=[x if x%10==0 else 0 for x in vector ]
print(hola)
