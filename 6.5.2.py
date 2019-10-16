'''''
Use a mask to multiply all values below 100 in the 
following list by 2:
repeat this until all values are above 100
Then, select all values between 150 < a < 200
'''''
import numpy as np


a = np.array([230, 10, 284, 39, 76])
cutoff = 100
#a[a<cutoff] = a[a<cutoff]*2

while ((a > 100).any()):

    a[a<cutoff] = a[a<cutoff]*2
    
    if (a > 100).all() : 
        break

print("\n")
print(a)
print("\n")
print(a[(a<200) & (a>150) ])