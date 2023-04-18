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
    print(F"\n\t{COL['yel']}=== PANDAS EXCERCISES ==={COL['b_n']}\n")

    # import system
    system('cls')

    print(f"\n{FR_YELL}Donostia camaras tráfico{NO_COLOR}\nReading JSON from url\n\thttps://www.donostia.eus/datosabiertos/recursos/camaras-trafico/camarastraficocas.json")
    URL = "https://www.donostia.eus/datosabiertos/recursos/camaras-trafico/camarastraficocas.json"
    result = requests.get(URL)
    print(f"\n{FR_YELL}requests response: {result}{NO_COLOR}")
    pause()

    cameras = result.text
    print(f"var cameras type: {str(type(cameras))}")
    print(f"\n{FR_YELL}camaras info\n{cameras}")
    pause()

    print(f"\n{FR_YELL}Convert in list of dicts with .json method{NO_COLOR}")
    cameras_list = result.json()
    print(f"\nvar cameras_list type: {str(type(cameras_list))}")
    print(cameras_list)
    # cameras_json = json.loads(cameras)  # not apply        
    pause()

    for json_el in cameras_list:
        print(f"data type: {str(type(json_el))}")
        print(f"Camara ubication: {json_el['Nombre']}\n\tLatitud {json_el['Latitud']} | Longitud {json_el['Longitud']}\n")    
    pause()

    print(f"\n{FR_YELL}Random with numpy{NO_COLOR}\n")

    random_list = np.random.randint(1000, size= 5)
    print(f"\nrandom list: {random_list}")

    series = pd.Series(random_list)
    print(f"\n-- series:\n{series}") 
    print(f"\n-- series[:]\n{series[:]}")   
    print(f"\n-- series.iloc[[2,4]]\n{series.iloc[[2,4]]}")
    print(f"\n-- series.head()\n{series.head()}")
    print(f"\n-- series.tail()\n{series.tail()}")
    

    print(f"\n{FR_YELL}Index with panda{NO_COLOR}\n")
    list=range(5)
    print(f"\n -- type of range(5): {str(type(list))}")
    series = pd.Series(random_list, index=["a","b","c","d","e"])
    print(f"\n -- series pd.Series(random_list, index=['a','b','c','d','e'])\n{series}")
    series = pd.Series(random_list, index=list)
    print(f"\n -- series pd.Series(random_list, index=list)\n{series}")
    print(f"\n -- series.head():\n{series.head()}")
    pause()


    print(f"\n{FR_YELL}DataFrames with panda{NO_COLOR}\n")
    acciones = {"SAN":[1,3.14,1], "REP": [1,14.1,2], "IBM":[1,129,3], "MSF":[1,2,3], "IBM1":[1,129,3], "MSF1":[1,2,3] }
    df = pd.DataFrame(acciones)
    print(f"type of var df: {str(type(df))}\n")
    print(f"df of acciones {acciones}\n{df}")

    df.head()
    # stadistic functions
    print(f"\n{FR_YELL}df.describe() statistics{NO_COLOR}\n{df.describe()}\n")
    # show rows...                           
    print(f"\ndf.loc[[1,2]]\n{df.loc[[1,2]]}")                           
    # show data for row where "REP" == 2    
    print(f"\ndf.loc[df['REP'] == 2]\n{df.loc[df['REP'] == 2]}")  
    # show columns REP, IBM               
    print(f"\ndf.loc[df['REP'] == 2, ['REP','IBM']]\n{df.loc[df['REP'] == 2, ['REP','IBM']]}")   


    print(f"\n{FR_YELL}read csv with panda and use DataFrames{NO_COLOR}\n")
    df = pd.read_csv("https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/fortune1000.csv")

    print(f"\ndf = pd.read_csv('https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/fortune1000.csv')\ntype: {str(type(df))}\n")
    print(f"\ndf.tail(10)\n{df.tail(10)}\n")
    print(f"\ndf.describe() - statistics\n{df.describe()}\n")
    print(f"\ndf.loc[[10,20,30]]\n{df.loc[[10,20,30]]}\n") 
    print(f"df.loc[10:20]\n{df.loc[10:20]}\n") 
    print(f"df.loc[500:504]\n{df.loc[500:504]}\n")
    print(f"df.iloc[500:504,0:3]\n{df.iloc[500:504,0:3]}\n")
    #df.loc[500:504,]
    #df.Company
    list_0_20 = df.loc[0:20]
    print(f"list_0_20 = df.loc[0:20]\n{list_0_20}")
    list_0_20.head()
    print(f"\nkeys of dict:\n\t{list_0_20.keys()}\n====================\n")
    list_0_20[["Company","Sector","Employees","Profits"]]
"""
    # plot_var method
    x_points = list_0_20.Employees
    y_points = list_0_20.Profits
    print(f"x_points:\n{x_points}\ny_points\n{y_points}")
    
    # plot x - y
    list_0_20.plot.bar(x="Employees",y="Profits")    

    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")
"""