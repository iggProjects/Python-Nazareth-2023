"""  
1.- This code is to pass the exercises to the teacher
2.- Page 75
"""
#
# IMPORT SECTION
#
from MyFunc_ForTeacher import *
from Colors_ForTeacher import *
from math import ceil

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    # ------------------- Nominas excercise ------------------

    class empleado:
        def __init__(self, name, cargo, salario):
            self.name = name
            self.cargo = cargo
            self.__salario = salario
        
        def empleadoInfo(self):
            salary = '{:,.2f}'.format(self.__salario * 1.1).replace(',','.')
            print("Empleado:", self.name, ", Cargo: ", self.cargo , ", Salario: ", salary, "\n")

    empleados = []

    Jon = empleado("Jon", "Programador python", 10000)
    Maria = empleado("María", "Programador java", 12000)
    Leo = empleado("Leo", "Programador HTML", 10000)
    
    empleados.append(Jon)
    empleados.append(Maria)
    empleados.append(Leo)


    # as it should be, it doesn't work if you call salario info from object
    """
    for empleado in self.empleados:
        empleado.salario
    """       

    class Sistema_nominas:

        def __init__(self,empleados):
            self.empleados=empleados

        def calcular_nominas(self):            
            print(f"{FR_GREEN}---- Calculando nominas de los empleados ----{NO_COLOR}\n")
            for empleado in self.empleados:
                empleado.empleadoInfo()



    nominas = Sistema_nominas(empleados)
    nominas.calcular_nominas()
    
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