#/!usr/bin/python3

class MyClass:
    def __init__(self):
        self.value = 0

my_objects = []

for i in range(100):
    my_objects.append(MyClass(i))

# later

for obj in my_objects:
    print obj.number

