import numpy as np

salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],[20.89,98.99,258.62,19.76,101.59],[70.66,190.10,134.54,200.14,15.59],[10.52,201.59,140.55,13.99,45.98]])

print("Step 1")
total_sales= np.sum(salesArray)
print("Total Sales for the store: $", round(total_sales, 2))

print()

print("Step 2")
min_sale= np.min(salesArray)
max_sale= np.max(salesArray)
print("Smallest sale: $", min_sale)
print("Largest sale: $", max_sale)
print()

print("Step 3")
g_sales= salesArray >= 100
print(g_sales)
print()

print("Step 4")
r_totals= np.sum(salesArray, axis= 1)
print("Total sales per register:")
print(r_totals)
print()

print("Step 5")
cfees_array= salesArray * .02
total_fees= np.sum(cfees_array)
print(cfees_array)
print("Total credit card fees: $", round(total_fees, 2))
print()

print("Step 6")
np_array= salesArray - cfees_array
print("Net profit without card fees:")
print(np_array)
print()

print("Step 7")
selected_registers= salesArray[[1, 3], :]
print("Sales for registers #2 and #4:")
print(selected_registers)
print()

print("Step 8")
newRegister = np.array([17.89,13.59,107.89,176.88,56.78])
salesArray= np.vstack([salesArray, newRegister])
print("Updated salesArray with the new register:")
print(salesArray)
print()

print("Step 9")
print("Before correction:")
print(salesArray[2])
salesArray[2, 3]= 20.14
print("After correction:")
print(salesArray[2])



