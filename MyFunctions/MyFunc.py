"""
 MY FUNCTIONS FOR:

   - see objects types, methods and attributes,
   - view objectS info in matrix form
   - time functions like pause, ......  
   - printing colors options
   - decisions functions
   - use HELP function
   - write in log files, like "comments log", "errors log"
   - OS most used functions
   - MODULES info

"""
#
# IMPORT LIBRERIES OR YOUR OWN FUNCTIONS 
#
"""
import Colors_in as Colors
   IMPORT CONFLICT -->  PROBLEM WHEN IS CALLED TWICE: ROOT DIR AND MYFUNCT DIR

"""

#
# COLORS CONSTANTS
#

# FOREGROUND CONSTANTS
def frGREEN(msg):  return f"\033[92m{msg} \033[00m"   # green
def frRED(msg):  return f"\033[91m{msg} \033[00m"   # red

# FOREGORUND CONSTANTS AS NUMBER
FG_RED          = 91
FG_GREEN        = 92
FG_YELLOW       = 93
FG_LIGHT_PURPLE = 94
FG_PURPLE       = 95
FG_CYAN         = 96
FG_LIGHT_GRAY   = 97
FG_BLUE         = 34   # ???
FG_BLACK        = 98

# FOREGORUND CONSTANTS AS TEXT
FG_WH_TXT = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
NO_COLOR = "\033[00m"

# BACKGROUND CONSTANTS
BG_BLACK  = 16
BG_BLUE   = 17
BG_RED    = 124
BG_ORANGE = 165

#
# COLOR PRINT FUNCTIONS
#
# foreground
def prFG(msg,col):
    col1 = str(col)
    return print(("\033[" + col1 + "m " + msg + " \033[0;0m\n"))

# background
def prBG(msg,col):
    col1 = str(col)
    return print(("\033[48;5;" + col1 + "m " + msg + " \033[0;0m\n"))
    #return(f"\033[48;5;{col1}m {col1} \033[0;0m\n".format(msg))

def prBG_orange(msg): 
    return print(("\033[48;2;255;165;0m {} \033[0;0m".format(msg)))


#
# TIME FUNCTIONS
#

# pause function
def pause():
  print()
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  
        

#
# DECISIONS FUNCTIONS
#        


# Check why not works with import model
def Y_N(msg):    
    print()    
    ans=str(input(msg))    
    if ans == 'N':                        
        return False
    elif ans == 'Y':                                
        return True
    else:
        Y_N(msg)


#
# PRINT VARS 
#

# print 'lists-tuples' in matrix form
def matrix_view(obj_l_t,n_cols):
  if 'list' in str(type(obj_l_t)) or 'tuple' in str(type(obj_l_t)):  # cambiar la pregunta
    import math
    matrix_rows=math.ceil(len(obj_l_t)/n_cols)
    lines=[]
    line=[]
    i=0
    for i in  range(matrix_rows):    
      for j in range(n_cols):
        if i*n_cols+j<len(obj_l_t):
          line.append(obj_l_t[i*n_cols+j])
      print(f"line: {i+1} --> {line}")
      line=[]  
  else:
    print(frRED(f"\nWarning FROM matrix_view(): Object '{obj_l_t}' in not  list neither tupla !\n" )) 

#
# SHOW LIBRARY INFO
#

# List Library Methods
# search name of module to abbreviate the print info
def library_methods(my_lib):
  for method in dir(my_lib):
    LIB_method  = method
    print(f"{FR_GREEN}{str(my_lib)}.method --> {NO_COLOR}´{LIB_method}")
  print()  

#
# SHOW OBJECTS INFO
#

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
  prBG("-----------------END MOSTRAR OBJECT TYPE AND ATTRIB-METHODS-----------------",17)    
  print()
  
# Show elements looking at dir(obj)
def ver_objetos(obj):
	enum=1
	si_color='\033[0;91m'
	no_color='\033[0m'
	print(si_color + 'TIPO:' + no_color, str(type(obj)) , '\n')
	for elemento in dir(obj):
		ver='obj.' + elemento
		print(str(si_color + 'Elemento: ' + str(enum) + ' ' + no_color + ver))
		if 'method' in str(eval(ver)):
			print('\tMetodo --> ', eval(ver))
		else:
			print('\tAtribu --> ', eval(ver))
			print('\tTipo --> ', type(eval(ver)), '\n')
		enum=enum+1


# More specific info for objects
def ver_elementos(obj, todo=True):
  enum=1
  print_count = 1
  si_color='\033[0;91m'
  no_color='\033[0m'
  # Coloreado Purpura \033[0;95m
  numb_elem=len(dir(obj))
  #print(f"object '{obj}' type '{type(obj)}' has {numb_elem} elements") 
  print(si_color + 'TIPO: ' + no_color + str(type(obj)) + '\n')
  print(si_color + 'DOC: ' + no_color + type(obj).__doc__ + '\n')
  
  for elemento in dir(obj):
    if todo == False and '_' in elemento:
      pass
    else:
      ver='obj.' + elemento      
      # Coloreado Rojo \033[0;91m
      si_color='\033[0;91m'
      print(si_color + 'Elemento ' + str(enum) + ': ' + no_color + ver + ' || '+ str(eval(ver)))      
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

      print(si_color + descripcion + ' --> ' + no_color + str(eval(ver)) )
      print(si_color + 'Tipo   --> ' + no_color + str(type(eval(ver))) )
      print(si_color + 'Doc    --> ' + no_color + str(eval(ver).__doc__) + '\n')
      enum=enum+1
      print_count += 1
      if print_count == 11:
          print_count = 1
          pause()

def help_obj_method(obj):
    print(help(type(obj)))    

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
#  LOG FILES FUNCTIONS
#

# writing comments in log file
def write_comments_log():
   print("here write_comments log file")

   
# redirect errors msg to 'own' errors log file
def write_comments_log():
   print("here my errors log file")

    
#
#  OS FUNCTIONS
#
















"""
    TESTING SECTION FOR DIFFERENT TYPES OF VARS
"""
#x = [0,1,2,3,4,'hola']
#x = {'user':'iñaki','passw':'xx' }
#x='123rty'


#matrix_view(x,6)
#mostrar(x)
#ver_objetos(x)
#ver_elementos(x)
#desc_obj_method(x)
#pause()
#print(frGREEN("\nthat's all 😎\n"))
#print(Colors.frGREEN("\nthat's all 😎\n"))
#help_obj_method(x)
