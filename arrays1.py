import numpy as np

print("Step 1")
a1= np.full((4,3),2)
print(a1)

print()

print("Step 2")
a2= np.arange(0, 120, 10).reshape(3,4)
print(a2)

print()

print("Step 3")
a3= a2.reshape(4, 3)
print(a3)

print()

print("Step 4")
a4= a3*3
print(a4)

print()

print("Step 5")
a5= a1*a2
print(a5)

print("An error occured becuase the shape of the arrays for a1 and a2 are different for them to be broadcast together, a1 and a3 shapes are different number of rows and columns")

print()

print("Step 6")
a6= a1*a3
print(a6)

print("This worked because both a1 and a3 shapes are the same, the same number of rows and columns, this allows them to be broadcast together")

