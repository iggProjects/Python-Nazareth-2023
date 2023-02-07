#!/usr/bin/python3

import sys

# param: 
module_to_check = (sys.argv[1])

try:
	import module_to_check
except ImportError:
	print (f"{module_to_check} is not installed")

# print(module_to_check.__version__)
	
