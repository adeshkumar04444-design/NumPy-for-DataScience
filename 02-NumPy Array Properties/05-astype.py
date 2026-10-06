#data type conversion
#arr_name.astype(datatype)
import numpy as np 

arr = np.array([1.2, 2.5, 3.8])
int_arr = arr.astype(int)

print(arr.dtype)
print(int_arr)
print(int_arr.dtype)

#Output: float
#        [1 2 3]
#        int
