"""
    Script 
    password registration for the first time
"""

# IMPORT
import re   
import MyFunctions.Colors as Col

# FUNCTIONS

def pw_input():
    try:     
        passw = str(input(Col.frGREEN("Please enter your password: ")))         
        return passw        
    except ValueError:
        # print('Please enter your name')
        Col.frGREEN("Please enter your name: ")    
        passw = str(input(Col.frRED("Please enter your password: "))) 

def password():
    global pw1,pw2,pwError,password_data
    print(Col.frGREEN("in password()"))
    pw1 = pw_input()
    print(Col.frGREEN(f"first value for password: {pw1} "))
    pw2 = pw_input()
    print(Col.frGREEN(f"first value for password: {pw1} ")) 
    if pw1 == pw2:
        password_data["passw"]=pw1
        pwError = True   

# MAIN
if __name__ == "__main__":
    # global variables
    pw1 = ''
    pw2 = ''
    pwError = False
    password_data = {'user':'iñaki','passw':'' }

    while not pwError:
        print("main")
        password()

print((Col.frGREEN(f"\n{password_data}\n")))
print((Col.frGREEN("\nThat's all for today... 👌")))



