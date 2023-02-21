# scrip para introducir edad de los trabajadores hasta que se decida parar

# rango edad aceptable 18-65 (incluidos)

"""
    as recursive funtion 
"""

def input_edad():
    global seguir,trabajadores
    trabajador = {"nombre":'',"edad":''}

    try:
        edad_trabaj=int(input("Por favor indique su edad (entre 18 y 65): "))
        if edad_trabaj in range(18,65):
            print(f"Edad introducida -> {edad_trabaj}")

            # codigo que actualiza BD
            # using var type dictionary
           
            trabajador["edad"] = edad_trabaj
            trabajadores.append(trabajador)

            rpta=str(input("\nDesea seguir incluyendo trabajadores (Y,N): "))
            print(f"Su rpta es: {rpta}\n")

            if rpta=="N":
                seguir=False

    except ValueError:
        print('Introduzca un número natural entre 18 y 65')
        input_edad()

if __name__ == "__main__":
    seguir=True
    trabajadores = []
    while seguir:    
        input_edad()
        
    print("\nsesión concluida por el usuario\n")        
    print(f"Lista de trabajadores: {trabajadores}")



