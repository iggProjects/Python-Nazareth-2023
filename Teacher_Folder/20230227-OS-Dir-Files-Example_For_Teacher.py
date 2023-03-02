"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#
#import MyFunctions.MyFunc as MyFunc
#import MyFunctions.Colors_out as Col
import math
import os
import platform

# CONSTANT SECTION
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"

#
# FUNCTIONS SECTION
#

# Yes-No function
def Y_N(msg):
    global moreData  
    print()  
    ans=str(input(msg))    
    if ans == 'N':                        
        moreData=False
    elif ans == 'Y':                                
        moreData=True
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
    myPath = os.getcwd()
    f = []
    for (dirpath, dirnames, filenames) in os.walk(myPath):
        f.extend(filenames)
        break
    print(f"{FR_GREEN}path -->{NO_COLOR} {myPath}\n")
    matrix_view(f,3)
    print(f"\n------------------------------------------------\n")

    parent = os.chdir('../')
    parentPath = os.getcwd()
    print(f"{FR_GREEN}parent path -->{NO_COLOR} {parentPath}\n")
    f = []
    for (dirpath, dirnames, filenames) in os.walk(parentPath):
        f.extend(filenames)
        break
    matrix_view(f,3)
    print(f"\n------------------------------------------------\n")

    # Library methods info 
    pause()
    library_methods(os)
    pause()
    library_methods(platform)

    
    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    Y_N_answer='N'
    #Y_N_answer=Y_N_2("Do you want to see vars characteristics? (Y,N): ")
    #Y_N_answer=MyFunc.Y_N("Do you want to see vars characteristics? (Y,N): ")
    moreData=False
    Y_N("Do you want to see vars characteristics? (Y,N): ")  # if answ is 'Y' -> moreData=True

    if moreData:    
        # Put here the object you want to analyze
        obj='HOLA' # for example   
        print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{obj}' ----------{NO_COLOR}\n")
        pause()
        # my objects functions  
        mostrar(obj)       

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()