__author__ = 'VarunPius'

#A = []

A = input("enter nos to be sorted:").split()

A = list(map(int, A))   # only map() in python 2
                        # A takes input as a string so we need to map it as integer;
                        #  can't use int(A) as A is a list and it can only be used on string not string list.
m = len(A)

'''
When we didn't map A[] into integer:
i/p: 65 45 6 18 2 87 62 498 12
o/p: ['12', '18', '2', '45', '498', '6', '62', '65', '87']
'''

for j in range (1,m):
    key = A[j]
    i = j-1
    while (i >= 0) and (A[i] > key):
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key
print (A[0:])


