"""
https://www.geeksforgeeks.org/print-colors-python-terminal/
https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
https://www.javatpoint.com/how-to-print-colored-text-in-python
https://gist.github.com/iansan5653/c4a0b9f5c30d74258c5f132084b78db9
https://gist.github.com/vratiu/9780109



Class COLORS for printing in console

Colors class:
    reset all colors with colors.reset;
    two sub classes fg for foreground and bg for background; 
    use as colors.subclass.colorname.
        i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable, underline, 
        reverse, strike through, and invisible work with the main class i.e. colors.bold
"""

class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m' 

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m' 
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m' 

"""
prints table of formatted text format options
"""
def print_format_table():
    for style in range(8):
        for fg in range(30, 38):            
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])                
                s1 += '\x1b[%sm %s \x1b[0m' % (format, 'hola')
                print(f"{format} -> {s1}")                
                #print(f"\t{s1}")
            #print(s1)            
        print('\n')

def print_format_table1():
    for style in range(1):
        for fg in range(30, 31):            
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])                
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(f"{format} -> {s1}")                
                #print(f"\t{s1}")
            #print(s1)            
        print('\n')


print(colors.bg.green, "SKk", colors.fg.red, "Amartya") 

#print(colors.bg.blue, colors.fg.red, "SKk Amartya",)
print(colors.bg.blue, "SKk", colors.fg.red, "Amartya")
print(colors.reset)

print_format_table()
# print_format_table1()

print('\x1b[0m Reset / Normal \x1b[0m')
print('\x1b[21m Doubly underline or Bold off \x1b[0m')
print('\x1b[31m Red foreground \x1b[0m')
print('\t\x1b[47m White background \x1b[0m')
print('\t\x1b[102m Bright Green background \x1b[0m')

print(colors.reset)

printString = ''
bgch = '--'
for i in range(0, 16):
    printString += f'\x1b[48;5;{i}m{bgch} abc \x1b[0m'
print(printString)

CSI = "\x1b["
print("\n" + CSI + "31;94m" + "Colored Text" + CSI + "0m")
print(f"\n{CSI}31;92mColored Text{CSI}0m")

def colors_text256(color_):  
    num1 = str(color_)  
    num2 = str(color_).ljust(3, ' ')  
    if color_ % 16 == 0:  
        return(f"\033[48;5;{num1}m {num2} \033[0;0m\n")  
    else:  
        return(f"\033[48;5;{num1}m {num2} \033[0;0m")  

 
print("\nThe 256 colors scheme is:")  
print('--'.join([colors_text256(x) for x in range(256)]))


# testing some values
print(''.join([colors_text256(16)]))
print(''.join([colors_text256(17)]))

# print(colors_text256(41))


def msg_colors_text256(msg,color_):  
    num1 = str(color_)  
    #num2 = str(color_).ljust(3, ' ')  
    if color_ % 16 == 0:  
        return(f"\033[48;5;{num1}m {msg} \033[0;0m\n")  
    else:  
        return(f"\033[48;5;{num1}m {msg} \033[0;0m")
    
"""
 16: bg black fg white
 17: bg blue  fg white
124: bg red   fg white
"""
print(msg_colors_text256('hy',16))
print(msg_colors_text256('hy',17))
print(msg_colors_text256('hy',124))
print(msg_colors_text256('hy',208))

print("\033[1;43m HELLO \n")

print(colors.reset)
#
