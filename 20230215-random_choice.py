import random


list=[1,2,3,4,5]
print(list)
my_value = random.choice(list)
print(f"my_value:  {my_value}")
i=1
#print("my_value: " + my_value)
while my_value != 5:
    i += 1
    my_value = random.choice(list)
    print(f"my_value:  {my_value}")

print(f"intento: {i} , my_value:  {my_value}")
