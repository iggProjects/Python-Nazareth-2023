# 
#    THIS SCRIPT IS FOR encrypt and decode texts
#

# IMPORT SECTION
import string
import random

# CONSTANT SECTION


# FUNCIONS SECTION

# pause function
def pause():
	userInput = input('Press ENTER to continue, or CTRL-C to exit\n')  

# colors functions
def frGREEN(msg):  return f"\033[92m{msg} \033[00m"   # green
def frRED(msg):  return f"\033[91m{msg} \033[00m"   # red

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
    print(frGREEN("\n---------- main ----------\n"))

    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    old_alphab = list(string.ascii_lowercase)
    print(frGREEN(f"old alphabet list\033[00m:➡ {old_alphab}\n"))
    
    # random.shuffle() to create new_alphab
    random.shuffle(old_alphab)
    new_alphab=old_alphab       
    print(frGREEN(f"new alphabet list\033[00m ➡ {new_alphab}\n"))
    pause()

    # my text
    my_text = 'abcdef ghijk lmnopq'
    print(frGREEN(f"my text ➡ \033[00m {my_text}\n"))

    # call encrypt function to change original text
    encripted_text = ''    
    encrypt(my_text,alphab,new_alphab)
    print(frGREEN(f"encrypted text ➡ \033[00m {encripted_text}\n"))    

    # decode process
    decoded_text=''
    decipher(encripted_text,new_alphab,alphab)
    print(frGREEN(f"decoded text ➡ \033[00m {decoded_text}\n"))
    print((frGREEN("\n---------- That's all for today 👌 ----------\n")))
    pause()

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    pause()