"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors_out as Col
import string
import random

# CONSTANT SECTION
NO_COLOR = "\033[00m"

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

# funtion to encrypt a text
def encrypt(text,alphab1,alphab2):
    global encripted_text 
    for ch in text:
        # find 'ch' in new_alphab 
        if ch in alphab1:
            ind = alphab1.index(ch) 
            encripted_text += alphab2[ind]
        elif ch == ' ':
            encripted_text += ch
        else:      
            pass    

def decipher(text,alphab1,alphab2):
    global decoded_text    
    for ch in text:
        # find 'ch' in new_alphab 
        if ch in alphab1:
            ind = alphab1.index(ch) 
            decoded_text += alphab2[ind]
        elif ch == ' ':
            decoded_text += ch
        else:      
            pass    

#
# ---------- MAIN ----------
#
if __name__ == "__main__":
    print(Col.frGREEN("\n---------- main ----------\n"))

    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    old_alphab = list(string.ascii_lowercase)
    print(Col.frGREEN(f"old alphabet list ➡  {NO_COLOR}{old_alphab}\n"))
    
    # random.shuffle() to create new_alphab
    random.shuffle(old_alphab)
    new_alphab=old_alphab       
    print(Col.frGREEN(f"new alphabet list ➡  {NO_COLOR}{new_alphab}\n"))
    

    # my text
    my_text = 'abcdef ghijk hello world'
    print(Col.frGREEN(f"my text ➡ {NO_COLOR} {my_text}\n"))

    # call encrypt function to change original text
    encripted_text = ''    
    encrypt(my_text,alphab,new_alphab)
    print(Col.frGREEN(f"encrypted text ➡ {NO_COLOR} {encripted_text}\n"))    

    # decode process
    decoded_text=''
    decipher(encripted_text,new_alphab,alphab)
    print(Col.frGREEN(f"decoded text➡  {NO_COLOR} {decoded_text}\n"))
    print((Col.frGREEN("\n---------- That's all for today 👌 ----------\n")))
    MyFunc.pause()
   
    # ------------------------------------------------
    #      IF YOU WANT, SHOW VARS CHARACTERISTICS 
    #------------------------------------------------- 
    
    Y_N_answer='N'
    moreData=False
    Y_N("Do you want to see vars characteristics? (Y,N): ")
    print(f"---- MAIN --- answer --> {moreData}\n")
    
    if moreData:
    #if Y_N_answer == 'Y':
        obj=''    # for example
        print((Col.frGREEN("\n---------- VARS CHARACTERISTICS ----------\n")))
        MyFunc.pause()
        MyFunc.mostrar(obj)
        MyFunc.desc_obj_method(obj)  
    else:
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------\n")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()