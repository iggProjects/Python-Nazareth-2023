from os import system
import random

# CONSTANTS
# Col_dict
COL = {'b_n':'\033[00m','red':'\033[91m','gr':'\033[92m','yel':'\033[93m'} 

# FR Colors
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[94m"
FR_YELL  = "\033[93m"

from MyFunc_ForTeacher import *
from Colors_ForTeacher import *

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")

def printMsg(msg):
    print(f"{FR_GREEN}{msg}{NO_COLOR}")

def print_BN(msg):
    print(f"{msg}")       

def th_2_dec(num):
    return "{0:,.2f}".format(num)

#
# ---------- EXAM EXCERCISE ----------
#

if __name__ == "__main__":
    print(f"\n{FR_GREEN}---------- CLASSES EXCERCISE ----------{NO_COLOR}\n")
    pause()

    class Producto:    

        def __init__(self, nombre, precio, cantidad): 

            # control first char of name
            if nombre[0].isupper():
                self.nombre = nombre             
            else:
                return print(f"\t{FR_RED} -- Error: {nombre}: El nombre del producto debe iniciar en mayúsculas{NO_COLOR}")
                # raise ValueError(f"El nombre del producto debe iniciar en mayúsculas")

            # control precio > 10
            if precio > 10:
                self.precio = precio             
            else:
                return print(f"\t{FR_RED} -- Error: {precio}: El precio del producto debe ser mayor a 10{NO_COLOR}")    
                #raise ValueError(f"{FR_RED} -- Error: El precio del producto debe ser mayor a 10")

            # control precio in (1,100)
            if cantidad in range(1,100):
                self.cantidad = cantidad             
            else:
                return print(f"\t{FR_RED} -- Error: {cantidad}\n\tLa cantidad a introducir debe ser estar entre 1 y 100{NO_COLOR}{NO_COLOR}")        
                #raise ValueError(f" -- Error: cantidad a introducir debe ser estar entre 1 y 100")
        
    Jean = Producto('Jean',20,50)
    print(f"\t'Jean' object:\n\t{vars(Jean)}\n\n")
    """
    for attr in dir(vaquero):
        if '__' not in attr:
            atrib_str = attr.split()
            atrib = atrib_str[0]
            print(f"\t{attr}: {vaquero} --- {atrib}")
    """        

    el_principito = Producto('el Principito',8,102)
    print(f"\t'Jean' object:\n\t{vars(el_principito)}\n\n")


    print()        

    """
    # my code
    # page 71
    class User:
        def __init__(self, name, mobile, age):
            self.name = name
            self.mobile = mobile
            self.age = age

        def __eq__(self,other):
            return self.name == other.name \
                    and self.mobile == other.mobile \
                    and self.age == other.age

        def __str__(self):
            return f"name:{self.name}, "\
                f"age:{self.age}, "\
                    f"mobile:{self.mobile}"


    user_1 = User("Jon","111",20)
    user_2 = User("Igg","222",20)
    print(user_1.age)    
    print(user_1==user_2)
    print(user_1.__str__())

    # -------------------perros-----------------

    print(f"\n-------------------perros-----------------------\n")

    class Perro:

        def __init__(self, nombre, edad, raza):
            self.nombre = nombre
            self.edad = edad
            self.raza = raza

    perros =[] 

    miles = Perro("Miles", 4, "Jack Russell Terrier")
    buddy = Perro("Buddy", 9, "Dachshund")
    jack = Perro("Jack", 3, "Bulldog")
    jim = Perro("Jim", 5, "Bulldog")

    perros.append(miles)
    perros.append(buddy)
    perros.append(jack)
    perros.append(jim)

    print(f"{FR_GREEN}perros list:{NO_COLOR}\n{perros}\n")

    for p in perros:
        print(f"El perro se llama {p.nombre} y es {p.raza}")

    print()    

    # -------------------Superhero-----------------
    print(f"\n-----------------Superhero---------------------\n")

    class Superhero:
        def __init__(self, name):
            self.__name = name

        def displayname(self):
            print("Hero:", self.__name, "\n")

    myHeroe = Superhero("Shaktiman")

    # in this case, printing proceeds
    myHeroe.displayname()

    # in this case, we will have an error
    print(f"{FR_GREEN}in this case, we will have an error\n---- myHeroe.__name can't be invoked ----{NO_COLOR}\n")
    print(myHeroe.__name)
    """

    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    yesss=True   
    while yesss:
        _msg = "Do you want to see attributes for a specific VAR ? (Y,N): "
        answer=Y_N_2(_msg)        
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':            
        # add question for name of var.....
        _what_var = str(input("What VAR ? "))
        try: 
            _what_var
            _my_Obj_name = eval(_what_var)
            print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()