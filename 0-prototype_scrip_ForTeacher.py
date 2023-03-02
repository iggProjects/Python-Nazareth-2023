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

# Y-N function
"""
def Y_N(msg):       
    ans=str(input(msg))    
    if ans == 'Y':
        return 'Y'
    elif ans == 'N':
        return 'N'        
    else:
        Y_N(msg)
"""
def Y_N(msg):
    ans=str(input(msg))    
    if ans == 'N':                        
        return False
    elif ans == 'Y':                                
        return True
    else:
        Y_N(msg)


#
# ---------- COURSE EXCERCISES ----------
#

if __name__ == "__main__":
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    # my code


    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    moreData = False
    print()
    print(f"moreData before: {moreData}")
    moreData = Y_N("Do you want to see vars characteristics? (Y,N): ")  # if answ is 'Y' -> moreData=True
    print(f"moreData after: {moreData}")

    if moreData:    
        obj='HOLA'    # for example
        print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{obj}' ----------{NO_COLOR}\n")
        pause()
        # my objects functions  
        mostrar(obj)       
    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()