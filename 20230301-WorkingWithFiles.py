"""  
THIS SCRIPT IS FOR MAKE BACKUP

# https://www.tutorialspoint.com/python/python_files_io.htm

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors_out as Col

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

"""
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
"""
#
# ---------- COURSE EXCERCISES ----------
#

if __name__ == "__main__":
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    MyFunc.pause()

    # my code

    # MAKING BACKUP OF A FILE

    # read file "agatha.txt"
    f = open("agatha.txt","r")
    #f = open(agatha.txt,"r")
    lines = f.readlines()

    # save info in list of lines "agathaLines"
    agathaLines=[]
    for line in lines:
        agathaLines.append(line)

    f.close()

    # create file copy agathaBkup.txt
    fBkup = open("agathaBackup.txt", "w")

    # write list in copy file
    for line in agathaLines:
        fBkup.write(line)

    print(fBkup.name)  

    fBkup.close()

    # reading backup file
    f = open("agathaBackup.txt","r")
    print(f"\n\033[91mprinting bakup file: {f.name}\033[00m\n")

    # read lines
    lines = f.readlines()

    # print lines of backup file
    print("\033[34m")
    for line in lines:  
        print(f"\t{line}")

    f.close()
    # return default color 
    print("\033[00m)")

    
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
        MyFunc.mostrar(obj)       
    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    MyFunc.pause()