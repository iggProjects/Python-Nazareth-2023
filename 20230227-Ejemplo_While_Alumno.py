#RETO 1

#1 introducir numero de transaciones hasta que el usuario no tenga mas, mostrar un informe del total de los numeros

"""
dinero_inicial = float(input("Cuanto dinero hay en la cuenta: "))#Iniciamos pewguntando el dinero de la cuenta y creamos las variables que vamos a usar
dinero_disponible=dinero_inicial
total_transacciones = 0.0
numero_transacciones = 0.0
ingresos = 0.0
retiros = 0.0
ing = 0
ret = 0
cantidades_ingresadas= []
cantidades_retiradas= []
while True:#iniciamos un bucle para realizar las preguntas
    pregunta = input("Quieres realizar una transaccion (s,n): ")#Primero preguntamos al usuario si quiere realizar una transaccion
    if pregunta=="s" or pregunta=="S":
        opcion = input("Quieres realizar un ingreso o retiro(i,r): ")#Si la respuesta es si preguntamos si queremos hacer un ingreso o retiro
        if opcion == "i" or pregunta=="I":
            transaccion = float(input("Indique la cantidad "))#Si hacemos un ingreso sumamos ese ingreso al saldo de la cuenta
            total_transacciones = total_transacciones+transaccion
            dinero_disponible = dinero_disponible + transaccion
            ingresos = ingresos+transaccion#Guardamos el ingreso en una lista para luego mostrarla y sumamos 1 al numero de transaciones echas
            numero_transacciones+=1
            ing+=1
            cantidades_ingresadas.append(transaccion)
        elif opcion == "r" or pregunta=="R":
            transaccion = float(input("Indique la cantidad "))#Si hacemos un retiro mayor al saldo de la cuenta indicamos que no es posible
            if transaccion > dinero_disponible:
                print("Saldo insuficiente")
            else:
                total_transacciones = total_transacciones-transaccion#Si hacemos un retiro restamos ese ingreso al saldo de la cuenta
                dinero_disponible = dinero_disponible-transaccion
                numero_transacciones+=1
                retiros = retiros-transaccion
                ret+=1
                cantidades_retiradas.append(transaccion)#Guardamos el retiro en una lista para luego mostrarla y sumamos 1 al numero de retiros realizados
        else:
            print("Respuesta incorrecta ")#Si no damos una respuesta valida lo indicamos para que el usuario lo sepa y volvemos a preguntar
    elif pregunta =="n" or pregunta=="N":#Si no queremos realizar mas transacciones
        print("El dinero inicial: " , dinero_inicial)#Mostramos el dinero inicial
        print("")
        print("Numero de ingresos: ", ing)#Mostramos cuantos ingresos se han hecho y sus cantidades
        print("Cantidades ingresadas: ")
        i = 0
        for i in cantidades_ingresadas:
            print(i)
        print("")
        print("Numero de retiros: ", ret)#Mostramos cuantos retiros se han hecho y sus cantidades
        print("Cantidades retiradas: ")
        i = 0
        for i in cantidades_retiradas:
            print(i)
        print("")
        print("El total de transacciones es: " , total_transacciones)#Mostramos el total de las transacciones realizadas
        media = (ingresos-retiros)/numero_transacciones
        print("La media de las transacciones es: ", media)#Mostramos la media de las transacciones
        print("")
        print("El saldo total de tu cuenta es: ", dinero_disponible)#Mostramos el saldo actual d la cuenta
        break
    else:
        print("Respuesta incorrecta")
"""

"""
   teacher example foramazon password case

"""        

# RESPUESTA AMAZON username y contraseñas
# funcion para validar el nombre, según la norma >= 6 caracteres
def validarNombre(nombre):
  LENGTH_NOMBRE = 6
  if len(nombre) < LENGTH_NOMBRE:
    return False
  else:
    return True

# funcion para validar la contraseña, según la norma >= 7 caracteres, not in lista de contrasseñas faciles
def validarPassword(password):
  LENGTH_PASSWORD = 7

  if password in ("password", "contraseña", "1234567", "qwerty"):
    print("La contraseña es demasiado fácil")
    return False
  elif len(password) < LENGTH_PASSWORD:
    print("La contraseña es muy corta ")
    return False
  else:
    return True


if __name__ == "__main__":

  valido = False
  while valido == False:
    nombre = input(
      "Introduce tu nombre, el nombre debe tener 6 o más caracteres ")
    valido = validarNombre(nombre)

  valido = False
  while valido == False:
    contrasena = input("Introduce tu contrasena ")
    valido = validarPassword(contrasena)

  print("Nombre y contraseña validos. Puedes entrar al programa ahora")
  print(f"Bienvenido {nombre} y contraseña {contrasena}")