import random

print("Ingrese Limite inferior")
LI=int(input())
print("Ingrese Limite superior (debe ser mayor al inferior)")
LS=int(input())

NR=random.randint(LI,LS)

while LS <= LI:
    print("El numero debe ser mayor al anterior")
    LS=int(input())


NR=random.randint(LI,LS)

    