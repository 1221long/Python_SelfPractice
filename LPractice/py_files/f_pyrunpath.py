#! python3

import os 
import sys

print(sys.path)
print("")
print("py run folder:",sys.path[0])
print("")
print("py run file path:",sys.argv[0])
print("")
print("__file Output:",__file__)
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))

print("done ...")