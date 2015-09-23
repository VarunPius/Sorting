__author__ = 'VarunPius'

#A = []     # this is not needed as python will automatically make it a list when we enter data next line
A = input("enter nos to be sorted:").split()

A = list(map(int, A))   # only map() in python 2
                        # A takes input as a string so we need to map it as integer;
                        # can't use int(A) as A is a list and it can only be used on string not string list.
                        # eg: x = int(input("Enter a number: "))
m = len(A)
