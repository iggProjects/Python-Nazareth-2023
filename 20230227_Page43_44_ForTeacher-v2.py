
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors as Col

# FUNCIONS SECTION

"""# Yes-No function
def Y_N(msg):
    global moreData    
    ans=str(input(msg))
    print(f"\t\tAnswer -> {ans}\n")  
    if ans == 'N':                        
        moreData=False
    elif ans == 'Y':                                
        moreData=True
    else:
        Y_N(msg)
"""
#
# ---------- MAIN ----------
#
if __name__ == "__main__":
    print(Col.frGREEN("\n---------- main ----------\n"))
    MyFunc.pause()

    # your code

    # test return statement
    print(f"MyFunc.return_5() --> {MyFunc.return_5()}\n")

    result = MyFunc.return_5()
    print(f"result --> {result}\n")

    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    #Y_N_answer='N'
    #Y_N_answer=Y_N_2("Do you want to see vars characteristics? (Y,N): ")
    #Y_N_answer=MyFunc.Y_N("Do you want to see vars characteristics? (Y,N): ")
    moreData=False    
    #moreData = MyFunc.Y_N("Do you want to see vars characteristics? (Y,N): ")
    #MyFunc.Y_N_1(moreData,"Do you want to see vars characteristics? (Y,N): ")
    #print(f"---- MAIN --- answer --> {moreData}\n")
    
    if moreData:
    #if Y_N_answer == 'Y':
        obj='HOLA'    # for example
        print((Col.frGREEN(f"\n---------- INFO FOR OBJECT '{obj}' ----------\n")))
        MyFunc.pause()
        MyFunc.mostrar(obj)
        MyFunc.desc_obj_method(obj)  
    else:
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()