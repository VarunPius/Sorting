__author__ = 'VarunPius'

#A = []
A = input("enter nos to be sorted:").split()

A = list(map(int, A))   # only map() in python 2
                        # A takes input as a string so we need to map it as integer;
                        #  can't use int(A) as A is a list and it can only be used on string not string list.
m = len(A)

'''
for i in range (0,m):
    for j in range(i+1,m):
        if A[j] < A[i]:
            A[i], A[j] = A[j],A[i]
'''
print (A[0:])