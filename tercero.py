Frase=input("ingrese frase")

c=0
v=0

for i in Frase: #i recorre la palabra
    if i.lower() in "aeiou":
        v=v+1
    c=c+1
print("cantidad de vocales", v)
print ("cantidad de caracteres", c)