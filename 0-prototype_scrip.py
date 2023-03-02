"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors as Col

# CONSTANT SECTION
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"

# FUNCIONS SECTION



#
# ---------- MAIN ----------
#
if __name__ == "__main__":

    print(Col.frGREEN("\n---------- main ----------\n"))
    MyFunc.pause()

    # your code




    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    moreData=False
    moreData=MyFunc.Y_N("Do you want to see vars characteristics? (Y,N): ")
    
    if moreData:    
        obj='HOLA'    # for example
        print((Col.frGREEN(f"\n---------- INFO FOR OBJECT '{obj}' ----------\n")))
        MyFunc.pause()
        MyFunc.mostrar(obj)
        MyFunc.desc_obj_method(obj)  
    else:
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------\n")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()

    