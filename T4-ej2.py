#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

i=int(input("primer numero: " ))
j=int(input("segundo numero: " ))

for num in range(i,j):
    if num%2==1:
        print(num)
        num+=1
print()

    