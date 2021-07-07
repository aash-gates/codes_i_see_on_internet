# A program to find the smallest number in the list

L = [30,40,10,20,50]

smallest = L[0]
for i in L:
     if smallest > i:
         smallest = i

print (smallest)
 