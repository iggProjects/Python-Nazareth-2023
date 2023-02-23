"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
#import MyFunctions.MyFunc as MyFunc
#import MyFunctions.Colors_out as Col

# CONSTANT SECTION


# FUNCIONS SECTION

# pause function
def pause():
	userInput = input('Press ENTER to continue, or CTRL-C to exit\n')  

# COLORS FUNTIONS
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

def desc_obj_method(obj,todo=True):
    
    method_founded = False
    enum=1
    print_count = 1
    si_color = '\033[0;91m'
    no_color = '\033[0m'
    descripcion = ''
    ver = ''
    print(si_color + 'TIPO: ' + no_color + str(type(obj)) + '\n')
    print(si_color + 'DOC: ' + no_color + type(obj).__doc__ + '\n')
    
    obj_method = str(input(frRED(f"what method of object '{obj}' you want to see?" )))
    #obj_method = str(input(Colors.frRED(f"what method of object '{obj}' you want to see?" )))
    print()
    #obj_method = str(input(f"what method of object '{obj}' you want to see? "))
    #print(Colors.frGREEN(f"\n\tobj method selected --> '{obj_method}'\n"))

    for elemento in dir(obj):
      if todo == False and '_' in elemento:
        pass
      else:       
        #print(f"\nelemento: {elemento} -- type {type(elemento)}\n")  
        #if obj_method in dir(elemento):
        if obj_method in elemento:     
          method_founded = True     
          ver='obj.' + elemento      
          # Coloreado Rojo \033[0;91m
          si_color='\033[0;91m'
          
          if 'method' in str(eval(ver)):
            # Coloreado Amarillo \033[0;93m
            si_color='\033[0;93m'
            descripcion='Metodo'
          elif 'function' in str(eval(ver)):
            # Coloreado Azul \033[0;94m
            si_color='\033[0;94m'
            descripcion='Funcion'
          elif 'class' in str(eval(ver)):
            # Coloreado Cyan \033[0;96m
            si_color='\033[0;96m'
            descripcion='Clase '
          else:
            # Coloreado Verde \033[0;92m
            si_color='\033[0;92m'
            descripcion='Atribu'

          #Colors.frGREEN(f"elemento {str(enum)}: {str(eval(ver))} \n")
          print(si_color + str(enum) + ': ' + ver + no_color + '\n')        
          # print(si_color + str(enum) + ': ' + ver + ' || ' + str(eval(ver)) + no_color + '\n')        
          print(si_color +  descripcion + ' --> ' + no_color + str(eval(ver)) )
          print(si_color +  'Tipo   --> ' + no_color + str(type(eval(ver))) )
          print(si_color +  'Doc    --> ' + no_color + str(eval(ver).__doc__) + '\n')
          enum=enum+1
          print_count += 1
          if print_count == 11:
              print_count = 1
              pause()

        else: 
           pass          
    
    if not method_founded:      
      print(frRED("\nthere is no such method 🙄\n"))
      #print(Colors.frRED("\nthere is no such method 🙄\n"))

#
# ---------- MAIN ----------
#
if __name__ == "__main__":
    print(frGREEN("\n---------- main ----------\n"))
    pause()

    # your code
    encripted_text = ''
    decoded_text = ''

    my_text = 'Mi buen amigo, como has estado?'
    print(frGREEN(f"orig text:\n {my_text}\n"))
    
    encrypt(my_text)
    print(frGREEN(f"encripted text:\n {encripted_text}\n"))
    
    decipher(encripted_text)
    print(frGREEN(f"decoded text:\n {decoded_text}\n"))

    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    
    moreData=False
    Y_N("Do you want to see vars characteristics? (Y,N): ")
    print(f"---- MAIN --- answer --> {moreData}\n")
    
    if moreData:
    #if Y_N_answer == 'Y':
        obj=my_text  # for example
        print((frGREEN("\n---------- VARS CHARACTERISTICS ----------\n")))
        pause()        
        desc_obj_method(obj)  
    else:
        print((frGREEN("\n---------- That's all for today 👌 ----------")))

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    pause()