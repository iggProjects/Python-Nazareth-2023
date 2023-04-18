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
    print(f"\n{FR_YELL}keys of dict:\n{NO_COLOR}{list_0_20.keys()}\n")
    list_0_20[["Company","Sector","Employees","Profits"]]

    # plot_var method
    x_points = list_0_20.Company
    #x_points = list_0_20.Employees
    y_points = list_0_20.Profits
    #print(f"x_points:\n{x_points}\ny_points\n{y_points}")
    
    # plot x - y
    list_0_20.plot.bar(x="Company",y="Profits")    
    #list_0_20.plot.bar(x="Employees",y="Profits")    

    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")
