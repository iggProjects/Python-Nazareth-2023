"""  
THIS SCRIPT IS FOR APPLY READ AND WRITE METHODS WITH FILES

"""
#
# IMPORT SECTION
#
#import MyFunctions.MyFunc as MyFunc
#import MyFunctions.Colors_out as Col
import math

# CONSTANT SECTION
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"

#
# FUNCTIONS SECTION
#

# Yes-No function
def Y_N(msg):
    ans=str(input(msg))    
    if ans == 'N':                        
        return False
    elif ans == 'Y':                                
        return True
    else:
        Y_N(msg)

# pause function
def pause():  
  userInput = input(f"\n{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

# Show attributes and methods avalaible for "obj"
def mostrar(obj):      

  if type(obj) in ['list','dict']:
    print(f"Object elements view in matrix form (8 columns by row)\n")
    matrix_view(obj,8)

  # obj type and mem dir
  print(f"Object type is {type(obj)} and mem dir is: {id(obj)}\n")
  # obj attributes
  # attributes = [attr for attr in dir(obj) if not attr.startswith('__')]
  attr_meth = [attr for attr in dir(obj)]
  # print attributes and methods in matrix form
  print(f"Object assigned attributes and methods are:\n")
  matrix_view(attr_meth,8)
  print()

# print 'lists-tuples' in matrix form
def matrix_view(obj_l_t,n_cols):
  if 'list' in str(type(obj_l_t)) or 'tuple' in str(type(obj_l_t)):      
    matrix_rows=math.ceil(len(obj_l_t)/n_cols)
    lines=[]
    line=[]
    i=0
    for i in  range(matrix_rows):    
      for j in range(n_cols):
        if i*n_cols+j<len(obj_l_t):
          line.append(obj_l_t[i*n_cols+j])
      print(f"line: {i+1} --> {line}")
      #print(f"line: {i+1} --> {line}\n")
      line=[]  
  else:
    print(f"\n{FR_RED}Warning FROM matrix_view(): Object '{obj_l_t}' in not  list neither tupla !{NO_COLOR}\n" ) 

# List Library Methods
def library_methods(my_lib):
  for method in dir(my_lib):
    LIB_method  = method
    print(f"{FR_GREEN}{str(my_lib)}.method --> {NO_COLOR}´{LIB_method}")

#
# ---------- COURSE EXCERCISES ----------
#

if __name__ == "__main__":
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    # my code

    #
    #  Reading and writing in files
    #

    f = open("agatha.txt","r")
    print(f.name)
    print(f.mode)
    text = f.read()

    text = f.read(30)  # read 30 chars
    print(text)

    lin1 = f.readline()
    print(f"line: {lin1}")
    lin1 = f.readline()
    print(f"line: {lin1}")

    lines = f.readlines()
    print(lines)
    print()

    i=1
    for l in lines:
      print(f"line: {i}, {l}")
      i+=1

    f.close()

    print(f.name)
    print(type(f))

    with open("agatha.txt","r+") as f:
      f.write("hola\n")

    f = open("agatha.txt","r")
    lines = f.readlines()
    i=1
    for l in lines:
      print(f"line: {i}, {l}")
      i+=1







    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    moreData = False
    print()
    moreData = Y_N("Do you want to see vars characteristics? (Y,N): ")  # if answ is 'Y' -> moreData=True

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