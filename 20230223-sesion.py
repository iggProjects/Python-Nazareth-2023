"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors_out as Col

# CONSTANT SECTION


# FUNCIONS SECTION

# Yes-No function
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

def printMsg(msg):
    print(Col.frGREEN(f"\nmessage is: {MyFunc.FG_WH_TXT} {msg}\n"))

def Sum_List(num_list):
    type_int = all(isinstance(x, int) for x in num_list)
    if type_int==True:              
        return print(f"Sum of the list elements {n_list} --> {Sum_List(num_list)}\n")
    else:
        return print(Col.frRED(f"Warning: in list {n_list} at least one item is not integer\n"))


#
# ---------- MAIN ----------
#
if __name__ == "__main__":

    print(Col.frGREEN("\n---------- MAIN ----------\n"))    
    # Print message    
    printMsg("hola\n")    
    MyFunc.pause()

    # print sum of items in a list of numbres
    n_list=[1,2,3,'x',5,6,7,8,9,10]
   
    Sum_List(n_list)

    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 

    MyFunc.pause()

    moreData=False
    Y_N("Do you want to see vars characteristics? (Y,N): ")
    #print(f"---- MAIN --- answer --> {moreData}\n")
    
    if moreData:
        obj=''    # for example
        print((Col.frGREEN("\n---------- VARS CHARACTERISTICS ----------\n")))
        MyFunc.pause()
        MyFunc.mostrar(obj)
        MyFunc.desc_obj_method(obj)  
    else:
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()