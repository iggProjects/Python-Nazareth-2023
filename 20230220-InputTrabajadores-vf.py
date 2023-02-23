# scrip for register worker data

# IMPORT
import re   
import MyFunctions.Colors_out as Col
import MyFunctions.MyFunc as MyFunc

# Y,N answer function
def Y_N():
    global moreData    
    ans=str(input("\nDo you want to continue including workers? (Y,N): "))
    print(f"\t\tAnswer -> {ans}\n")  
    if ans == 'N':                        
        moreData=False
    elif ans == 'Y':                                
        input_worker_data()
    else:
        Y_N()

# Asking worker age
def input_worker_age():
    global moreData,workers,worker    
    try:
        worker_age=int(input(Col.frRED("\nPlease indicate \"age\" (integer between 18-65): ")))
        if worker_age in range(18,65):
            print(Col.frRED(f"\t\tage entered -> {worker_age}")) # next version: redirect a log file for answer
            # DB code or use var type dictionary to print data session
            worker["age"] = worker_age
            workers.append(worker)
            # ask for continue (Y,N)
            Y_N()
        else:
            Col.frRED("\nPlease indicate \"age\" (integer between 18-65): ") 
            input_worker_age()    
    except ValueError:
        Col.frRED("\nPlease indicate \"age\" (integer between 18-65): ")
        #print('please indicate age (integer between 18-65)')
        input_worker_age()

def input_worker_data():
    global moreData, workers, worker
    worker = {"name":'',"age":''}   
    # first try for worker name
    try:        
        #name_worker=str(input("\033[94mPlease enter your name: \033[00m"))               
        worker_name = str(input(Col.frGREEN("Please enter your name: ")))     
        # check characters
        if re.match("^[A-Za-zñáéíóúü]*$", worker_name):      
            print(Col.frGREEN(f"\t\tname -> {worker_name}"))  # next version: redirect a log file for answer
            # code to update DB or create a list with data type dictionary            
            worker["name"] = worker_name
            # call age funtion
            input_worker_age()            
    except ValueError:
        # print('Please enter your name')
        Col.frGREEN("Please enter your name: ")
        input_worker_data()

# MAIN
if __name__ == "__main__":
    # global variables
    moreData=True
    workers = []
    worker = {"name":'',"age":''}

    # loop until stop is "Y"
    while moreData:    
        input_worker_data()     

    print("\nsession terminated by user\n")        
    print(f"Workers is {type(workers)}:\n\t{workers}\n")
    for i in range(len(workers)):
        print(f"{workers[i]}, and data type is: {type(workers[i])}")
        print(f"\tworker {i}:")
        for key,value in workers[i].items():
            print(f"\t\t{key}: {value}")

    # SHOW VARS CHARACTERISTICS 
    print((Col.frGREEN("\n---------- VARS CHARACTERISTICS ----------\n")))
    MyFunc.pause()
    MyFunc.mostrar(workers)
    MyFunc.desc_obj_method(workers)    

else:
    # something wrong
    print(f"upsssssssss")

