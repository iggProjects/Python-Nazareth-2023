"""
    examples: while with else page 27
"""

# contando desde 100 hasta 50
i = 100
while (i>=50):
    if i%4 == 0:
        print(f"i: {i}, es un múltiplo de 4 que es mayor o igual a 50 y menor q 100.")
    i = i-1
print("-----------------------\n")

# multiples of 4
i = 20
def multiple_of(n,number):
    
    if number % 4 == 0:        
        if number%n == 0:
            return(f"{number} is a multiple of {n}\n")
        else:
            return(f"{number} isn't a multiple of {n}\n")                
    else:        
        if number%n == 0:
            return(f"{number} is a multiple of {n}")
        else:
            return(f"{number} isn't a multiple of {n}")            

print(' -- '.join([multiple_of(4,x) for x in range(i)]))


#Como un estudiante de matemáticas, quiero imprimir todos los números de 0 a 99
#   excluyendo (10, 20, 30, 40, 50, 60, 70, 80, 90) y usando un bucle WHILE

for i in range(30):
    if i not in (10, 20) and i%2 == 0:
        print(i)

print("-----------------------\n")

i = 0
while i < 40:
    if i not in (10, 20, 30, 40, 50, 60, 70, 80, 90) and i % 3 == 0:
        print(i)
    i = i +1
else:
    print(f"leaving while 100\n")
