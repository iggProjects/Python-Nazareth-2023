"""
 My functions to;
   - see objects methods and attributes,
   - view object info in matrix form
   - pause printing
   - use HELP function

"""

# IMPORT
import Colors

# pause function
def pause():
	userInput = input('Press ENTER to continue, or CTRL-C to exit ');

# print 'lists-tuples' in matrix form
def matrix_view(obj_l_t,n_cols):
  import math
  # checking if obj_list is type 'list-tuple'
  # if ():  
  matrix_rows=math.ceil(len(obj_l_t)/n_cols)
  lines=[]
  line=[]
  i=0
  for i in  range(matrix_rows):    
    for j in range(n_cols):
      if i*n_cols+j<len(obj_l_t):
        line.append(obj_l_t[i*n_cols+j])
    print(f"line: {i+1} --> {line}\n")
    line=[]  

# Show attributes and methods avalaible for "obj"
def mostrar(obj):  
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
  print(f"-----------------END MOSTRAR()-----------------\n")  

# 
# Show elements looking at dir(obj)
# 

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

#
# More specific than other functions
#

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
    
    obj_method = str(input(Colors.frRED(f"what method of object '{obj}' you want to see?" )))
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
      print(Colors.frRED("\nthere is no such method 🙄\n"))


#x=[0,1,2,3,4,'hola']
x='123rty'

mostrar(x)
#ver_objetos(x)
#ver_elementos(x)
desc_obj_method(x)
pause()
print(Colors.frGREEN("\nthat's all 😎\n"))
#help_obj_method(x)
