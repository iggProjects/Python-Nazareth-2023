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

# print char by char
def print_char_by_char(my_text):
    for ch in my_text:
        print(ch)

# funtion to encrypt a text
def encrypt(text,key_List):
    global encripted_text      
    text=text.replace('a','128') 
    text=text.replace('b','129')
    text=text.replace('c','130')    
    encripted_text=text

def decipher(text,key_List):
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

    # create list of alphabet and its ascii associated
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    list_alphab = list(string.ascii_lowercase)
    print(Col.frGREEN(f" {list_alphab}\n"))
    list_ascii_assoc = [ ord(lt)+10 for lt in list_alphab ]
    print(Col.frRED(f" {list_ascii_assoc}\n")) 
    # create a dictionary
    keyDict = dict(zip(list_alphab,list_ascii_assoc))
    print(Col.frGREEN(f"keyDict 👇👇\n\n {keyDict}\n")) 

    MyFunc.pause()

    # Call encrypt process 
    encripted_text = ''
    my_text = 'Mi buen amigo, como has estado?'
    print(Col.frGREEN(f"orig text:\n {my_text}\n"))    
    encrypt(my_text,keyDict)
    print(Col.frGREEN(f"encripted text:\n {encripted_text}\n"))

    # call decode process
    decoded_text = ''
    decipher(encripted_text,keyDict)
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
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------\n")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()