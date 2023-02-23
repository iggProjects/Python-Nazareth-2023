"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors_out as Col
import string

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

#
# ---------- MAIN ----------
#
if __name__ == "__main__":
    print(Col.frGREEN("\n---------- main ----------\n"))
    MyFunc.pause()

    # your code
    # chars asci values
    
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    list_alphab = list(string.ascii_lowercase)
    print(Col.frGREEN(f" {list_alphab}\n"))
    list_ascii_assoc = [ ord(lt) for lt in list_alphab ]
    print(Col.frGREEN(f" {list_ascii_assoc}\n")) 


    print((Col.frGREEN("\n---------- That's all for today 👌 ----------")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()