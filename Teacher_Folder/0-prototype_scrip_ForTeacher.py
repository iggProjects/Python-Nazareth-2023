"""  
1.- This code is to pass the exercises to the teacher
2.- The SCRIPT is for:
    2.1.-
    2-2.-
    .
    .

"""
#
# IMPORT SECTION
#
from MyFunc_ForTeacher import *
from Colors_ForTeacher import *
from math import ceil

#
# ---------- COURSE EXCERCISES ----------
#

if __name__ == "__main__":
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    # my code

    _someVar = [1,2,3,5]
    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    
    yesss=True   
    while yesss:
        _msg = "Do you want to see attributes for a specific VAR ? (Y,N): "
        answer=Y_N_2(_msg)        
        # add question for name of var.....
        _what_var = str(input("What VAR?"))
        _my_Obj_name = eval(_what_var)
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':            
        print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
        pause()
        # my objects functions  
        mostrar(_my_Obj_name)       
    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()