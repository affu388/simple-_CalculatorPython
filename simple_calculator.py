#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lovef
#
# Created:     30-09-2023
# Copyright:   (c) lovef 2023
# Licence:     <your licence>
#----------------------------------------------------------------------------
first = input("enter ypur first number:")
oprator =input("enter your opration (+,-,*,/,%):")
second =input("enter ypur second number:")
first=int(first)
second=int(second)
if oprator == "+" :
    print(first + second)
elif oprator == "-" :
    print(first - second)
elif oprator == "*" :
    print(first * second)
elif oprator == "/" :
    print(first / second)
elif oprator == "%" :
    print(first & second)
else :
    print("invalid oprator")