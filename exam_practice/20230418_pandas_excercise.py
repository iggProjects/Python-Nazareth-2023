"""
20230329_30-DataAnalysis.ipynb
"""

from os import system
import random
import requests
import pandas as pd
import numpy as np
import matplotlib as plt    


# CONSTANTS
# Col_dict
COL = {'b_n':'\033[00m','red':'\033[91m','gr':'\033[92m','yel':'\033[93m'} 

# FR Colors
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[94m"
FR_YELL  = "\033[93m"

# pause function
def pause():  
  userInput = input(f"\n{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")

def printMsg(msg):
    print(f"{FR_GREEN}{msg}{NO_COLOR}")

def print_BN(msg):
    print(f"{msg}")       

def th_2_dec(num):
    return "{0:,.2f}".format(num)
    

if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}=== TITLE ==={COL['b_n']}\n")


    # import system
    system('cls')

    URL = "https://www.donostia.eus/datosabiertos/recursos/camaras-trafico/camarastraficocas.json"
    result = requests.get(URL)

    cameras = result.text
    print(f"var cameras type: {str(type(cameras))}")
    # print(cameras)

    cameras_list = result.json()  

    # cameras_json = json.loads(cameras)  # not apply 
    print(f"var cameras_list type: {str(type(cameras_list))}")
    #print(cameras_list)

    for json_el in cameras_list:
        # print(f"camera: {str(type(json_el))}")
        print(f"Camera ubication: {json_el['Nombre']}\n\tLatitud {json_el['Latitud']} Longitud {json_el['Longitud']}")

    
    pause()

    random_list = np.random.randint(100, size= 5)
    series = pd.Series(random_list)
    print(f" -- series\n{series}")
    print("\n============\n")
    print(f" -- series.iloc[[2,4]]\n{series.iloc[[2,4]]}")
    print(F" -- series.head()\n{series.head()}")
    series[:]
    list=range(5)
    print(f" -- type of range(5):  {str(type(list))}")
    series = pd.Series(random_list, index=["1","2","3","4","5"])
    print(f"ºn -- series\n{series}")
    print(f"\n -- series.head():\n{series.head()}")


    acciones = {"SAN":[1,3.14,1], "REP": [1,14.1,2], "IBM":[1,129,3], "MSF":[1,2,3], "IBM1":[1,129,3], "MSF1":[1,2,3] }
    df = pd.DataFrame(acciones)
    print(f"type of var df: {str(type(df))}")
    print(df)

    df.head()
    df.describe()           # stadistic functions
    df.loc[[1,2]]           # show rows...
    df.loc[df["REP"] == 2]  # show data for row where "REP" == 2
    df.loc[df["REP"] == 2, ["REP","IBM"]]   # show columns REP, IBM


    df = pd.read_csv("https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/fortune1000.csv")

    print(f"df type: {str(type(df))}")
    df.tail(10)
    df.describe()
    df.loc[[10,20,30]] 
    df.loc[10:20] 
    df.loc[500:504]
    df.iloc[500:504,0:3]
    #df.loc[500:504,]
    #df.Company
    list_0_20 = df.loc[0:20]
    list_0_20.head()
    print(f"keys of dict: {list_0_20.keys()}\n==========\n")
    list_0_20[["Company","Sector","Employees","Profits"]]

    # plot_var method
    x_points = list_0_20.Employees
    y_points = list_0_20.Profits

    #print(x_points)
    list_0_20.plot.bar(x="Employees",y="Profits")    
    print(list_0_20.plot.bar(x="Employees",y="Profits"))

    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")