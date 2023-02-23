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

# print char by char
def print_char_by_char(my_text):
    for ch in my_text:
        print(ch)

# funtion to encrypt a text
def encrypt(text):
    global encripted_text        
    #list_changes_chars = {'a':128, 'b':129, 'c':130}    
    text=text.replace('a','128') 
    text=text.replace('b','129')
    text=text.replace('c','130')    
    encripted_text=text

def decipher(text):
    global decoded_text    
    text=text.replace('128','a')
    text=text.replace('129','b')
    text=text.replace('130','c')    
    decoded_text = text

#
# ---------- MAIN ----------
#
if __name__ == "__main__":
    print(Col.frGREEN("\n---------- main ----------\n"))
    MyFunc.pause()

    # your code
    encripted_text = ''
    decoded_text = ''

    my_text = 'Mi buen amigo, como has estado?'
    print(Col.frGREEN(f"orig text:\n {my_text}\n"))
    
    encrypt(my_text)
    print(Col.frGREEN(f"encripted text:\n {encripted_text}\n"))
    
    decipher(encripted_text)
    print(Col.frGREEN(f"decoded text:\n {decoded_text}\n"))

    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    Y_N_answer='N'
    #Y_N_answer=Y_N_2("Do you want to see vars characteristics? (Y,N): ")
    #Y_N_answer=MyFunc.Y_N("Do you want to see vars characteristics? (Y,N): ")
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
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()