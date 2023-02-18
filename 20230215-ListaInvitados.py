"""
  Making a guest list    
"""

# constants 
# maximun number of guests
MAX_GUESTS=3

# add colors to print
# https://www.geeksforgeeks.org/print-colors-python-terminal/
color_Y='\033[0;94m'
color_N='\033[0m'

# variables
ghests_list=[]    # list
i=0               # iterator  
completed=False   # boolean flag

while completed==False:
  name=input("Please give the name: ")
  ghests_list.append(name)
  #i=i+1
  i+=1
  if i==MAX_GUESTS:
    completed=True
    print(color_Y)
    print("The list is completed")      
print(f"\nGhests list: {ghests_list}" )