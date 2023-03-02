
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors as Col

#
# ---------- MAIN ----------
#

if __name__ == "__main__":
    print(Col.frGREEN("\n---------- main ----------\n"))
    MyFunc.pause()

    # ------------------------------------------------
    #           ASKING FOR SHOW VARS INFO 
    #------------------------------------------------- 

    # with Y_N_2 function
    yesss=True   
    while yesss:
        answer=MyFunc.Y_N_2("Do you want to see vars characteristics? (Y,N): ")        
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':    
        obj='HOLA'    # for example
        print((Col.frGREEN(f"\n---------- INFO FOR OBJECT '{obj}' ----------\n")))
        MyFunc.pause()
        MyFunc.mostrar(obj)
        MyFunc.desc_obj_method(obj)  
    else:
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    MyFunc.pause()