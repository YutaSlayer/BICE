Candidato1="Pedro"
Candidato2="Juan"

V1=int()
V2=int()
NU=int()

print("Ingrese la cantidad de votantes")
N1=int(input())

for N1 in range(N1):
    print("por quien voto este votante?")
    print("1-",Candidato1)
    print("2-",Candidato2)
    print("Otro numero sera nulo")
    N2=int(input())
    if N2 == 1:
      V1=V1+1
    elif N2 == 2:
       V2=V2+1
    else:
       NU=NU+1

if V1>V2:
   print(Candidato1,"Es el ganador")
elif V2>V1:
   print(Candidato2,"Es el ganador")
else:
   print("Empate")
   
print(Candidato1,":",V1)
print(Candidato2,":",V2)
print("Votos Nulos:",NU)