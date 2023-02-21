# scrip para introducir edad de los trabajadores hasta que se decida parar

# rango edad aceptable 18-65 (incluidos)

"""
    as recursive funtion 

    regex
        import re
        if not re.match("^[A-Za-z]*$", user_name):
"""

# IMPORT
import re   
import MyFunctions.Colors as Col

def input_worker_data():
    global moreData,workers
    worker = {"name":'',"age":''}

    # first try for name
    try:
        
        #name_worker=str(input("\033[94mPlease enter your name: \033[00m"))               
        name_worker=str(input(Col.frGREEN("Please enter your name: ")))       
        
        # check characters
        if re.match("^[A-Za-zñáéíóúü]*$", name_worker):
      
            print(Col.frGREEN(f"\tname -> {name_worker}"))

            # code to update DB or create a list with data type dictionary            
            worker["name"] = name_worker
            workers.append(worker)

            ans=str(input("\nDo you want to continue including workers? (Y,N): "))
            print(f"Your answer: {ans}\n")

            if ans=="N":
                moreData=False

    except ValueError:
        print('Please enter your name')
        input_worker_data()

if __name__ == "__main__":
    moreData=True
    workers = []
    while moreData:    
        input_worker_data()
        
    print("\nsesión concluida por el usuario\n")        
    print(f"Worker List: {workers}")
