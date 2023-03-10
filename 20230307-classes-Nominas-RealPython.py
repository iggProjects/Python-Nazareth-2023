"""  
    1.- This code is to pass the exercises to the teacher
    2.- Page 75 (nominas example)
    3.- reference: https://realpython.com/inheritance-composition-python/
"""
#
# IMPORT SECTION
#

from os import system
from MyFunctions import MyFunc
from MyFunctions import Colors
#from MyFunc_ForTeacher import *
#from Colors_ForTeacher import *

#
# ---------- COURSE EXCERCISE ----------
#

# decision function
def Y_N_2(msg):
    return str(input(msg))

#  Class Hierarchies
class SistemaNominas:
    def calculo_nomina(self, empleados):
        for empleado in empleados:
            nomina_emp = '{:,.2f}'.format(empleado.calculo_nomina()).replace(',','.')
            print(f"{Colors.FR_GREEN}\t{empleado.nombre} ({empleado.id}) | cargo '{empleado.cargo}'{Colors.NO_COLOR}\n\t\tpago: {nomina_emp}\n")            

class Empleado:
    #def __init__(self, id, nombre):
    def __init__(self, id, nombre, año_ncto, dir_resid, cargo):
        self.id = id
        self.nombre = nombre
        self.fec_ncto = año_ncto
        self.dir_resid = dir_resid
        self.cargo = cargo


class SalarioEmpleado(Empleado):
    def __init__(self, id, nombre,año_ncto,dir_resid,cargo,salario):
        super().__init__(id, nombre,año_ncto,dir_resid,cargo)
        self.salario = salario

    def calculo_nomina(self):
        return self.salario

class Comercial(SalarioEmpleado):
    def __init__(self, id, nombre,fec_ncto,dir_resid,cargo,salario,commision_ventas):
        super().__init__(id, nombre,fec_ncto,dir_resid,cargo, salario)
        self.commision_ventas = commision_ventas

    def calculo_nomina(self):
        fijo = super().calculo_nomina()
        return fijo + self.commision_ventas


if __name__ == "__main__":

    system('cls')

    print(f"\n{Colors.FR_GREEN}---------- main ----------{Colors.NO_COLOR}\n")
    MyFunc.pause()

    Empleados_empresa = []
    Empleados_empresa.append(SalarioEmpleado(1, 'Iñaki','1959','Errenteria','programador html',1500))
    Empleados_empresa.append(SalarioEmpleado(2, 'Xabier','1990','Donostia','programador java',1700))
    Empleados_empresa.append(SalarioEmpleado(3, 'Pedro', '1965','Donosita','programador python',2000))  

    Comerciales_empresa = []
    Comerciales_empresa.append(Comercial(4, 'Che','','','ventas empresas grandes',2500, 250,))
    Comerciales_empresa.append(Comercial(5, 'Oihana','','','staff marketing',3500, 500))

    print(f'\n{Colors.FR_BLUE}======= Calculando Nómina General ========{Colors.NO_COLOR}\n')
    
    corrida_nomina = SistemaNominas()

    print(f"\n\t{Colors.FR_BLUE}=== Grupo Oficinas ==={Colors.NO_COLOR}\n")
    for empl in Empleados_empresa:
        corrida_nomina.calculo_nomina([empl])  

    print(f"\n\t{Colors.FR_BLUE}=== Grupo Comerciales ==={Colors.NO_COLOR}\n")
    for comercial in Comerciales_empresa:
        corrida_nomina.calculo_nomina([comercial])  
    print(f"{Colors.FR_GREEN}\n======= Fin Corrida Nómina Empresa =======\n{Colors.NO_COLOR}")    


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
            print(f"\n{Colors.FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{Colors.NO_COLOR}\n")
            MyFunc.pause()
            # my objects functions  
            MyFunc.mostrar(_my_Obj_name)       

        except NameError:
            print(f"\n\t{Colors.FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{Colors.FR_GREEN}--------------- That's all for today 👌 ---------------{Colors.NO_COLOR}\n")

    else:
        print(f"\n{Colors.FR_GREEN}---------- That's all for today 👌 ----------{Colors.NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{Colors.FR_RED}---- upsssssssss something is wrong 😢😢  ---{Colors.NO_COLOR}\n")
    MyFunc.pause()