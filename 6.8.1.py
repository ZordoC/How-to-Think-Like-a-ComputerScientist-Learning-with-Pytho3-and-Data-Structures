import numpy as np 

'''''
This was a nightmare do not use any(a) > 200 
it won't work ever.



'''''



a = np.array([1,45,37],dtype='uint8')


while ((a < 200).any()):

    a=a+20


print(a)