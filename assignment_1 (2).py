# -*- coding: utf-8 -*-
"""Assignment 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11fSmTwIMGiXxhy2MW6MACBEVO9EDQpAA
"""

#adding two array
import numpy as np
my_list =[1,2]
my_item=[3,4]
np1=np.array(my_list)
np2=np.array(my_item)
print(np.add(np1,np2))

#Subtracting two arrray
import numpy as np
my_list =[5,3]
my_item=[3,4]
np1=np.array(my_list)
np2=np.array(my_item)
print(np.subtract(np1,np2))

#Multiplication two arrray
import numpy as np
my_list =[5,3]
my_item=[3,4]
np1=np.array(my_list)
np2=np.array(my_item)
print(np.multiply(np1,np2))

#Division two arrray
import numpy as np
my_list =[15,8]
my_item=[3,4]
np1=np.array(my_list)
np2=np.array(my_item)
print(np.divide(np1,np2))

#exponential of number
import numpy as np
my_list =[1,2]
np1=np.array(my_list)
print(np.exp(np1))

#Squareroot of number
import numpy as np
my_list =[5,6,7,8]
np1=np.array(my_list)
print(np.sqrt(np1))

#Element-wise: a==b

import numpy as np
 
an_array = np.array([[1, 2], [3, 4]])
another_array = np.array([[1, 2], [3, 4]])
 
comparison = an_array == another_array
equal_arrays = comparison.all()
 
print(equal_arrays)

# Array-wise: np.array_equal(a,b)

import numpy as np
 
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
 
 
# Comparing the arrays
if np.array_equal(arr1, arr2):
    print("Equal")
else:
    print("Not Equal")

#Copying an array
import numpy as np
np1=np.array([1,2,3,4,5,6,7])
np2=np.copy(np1)
print(f'original np1 ={np1}')
print(f'Original np2 ={np2}')
np1[0]=20
print(f'Changed np1 ={np1}')
print(f'Original np2 ={np2}')

#View an array
import numpy as np
np1=np.array([1,2,3,4,5,6,7])
np2=np1.view()
print(f'original np1 ={np1}')
print(f'Original np2 ={np2}')
np1[0]=20
print(f'Changed np1 ={np1}')
print(f'Original np2 ={np2}')

#Sort an array
import numpy as np
np1=np.array([5,9,4,1,53,64,70])
np2=np.sort(np1)
print(np2)

#Sort an array
import numpy as np
np1=np.array([5,9,4,1,53,64,70])
np2=np.sort(np1)
print(np2)

#sort according to axis
import numpy as np
np1=np.array([[3,4,5],[2,7,8]])
print(np.sort(np1,axis=0))

#reshape of array 
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
np2=np1.reshape(3,3)
print(np2)

#append an element 
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
np2=np.append(np1,10)
print(np2)

#insert an element 
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
np2=np.insert(np1,4,10)
print(np2)

# Deletes row on index 2 of array
import numpy as np
np1=np.array([[1,2],[5,6],[7,8]])
np2=np.delete(np1,2,axis=0)
print(np2)

#Deletes column on index 3 of array
import numpy as np
np1=np.array([[1,2,3,4],[5,6,10,11],[7,8,12,13]])
np2=np.delete(np1,3,axis=1)
print(np2)

#Adds array2 as rows to the end of array1
import numpy as np
my_list =[5,3]
my_item=[3,4]
np1=np.array(my_list)
np2=np.array(my_item)
np3=np.concatenate((np1,np2),axis=0)
print(np3)

#Adds array2 as columns to end of array1
import numpy as np
my_list =[[5,3],[6,7]]
my_item=[[3,4],[2,1]]
np1=np.array(my_list)
np2=np.array(my_item)
np3=np.concatenate((np1,np2),axis=1)
print(np3)

#Splitting of array 
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
np2=np.split(np1,3)
print(np2)

#Assigns array element on index 0 the value 5
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
np1[0]=5
print(np1)

#a[2,3]=1 - Assigns array element on index [2][3] the value 1
import numpy as np
np1=np.array([[1,2,3,4],[5,6,10,11],[7,8,12,13]])
np1[2,3]=1
print(np1)

#Returns the element of index 2 in array a.
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
print(np1[2])

#Returns the 2D array element on index [3][5]
import numpy as np
np1=np.array([[1,2,3,4,9,6],[5,6,10,11,76,4],[7,8,12,13,66,99],[3,2,55,66,78,99]])
print(np1[3,5])

#Returns the elements at indices 0,1,2,3
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
print(np1[0:4])

# Returns the elements on rows 0,1,2,3 at column 3
import numpy as np
np1=np.array([[1,2,3,4,9,6],[5,6,10,11,76,4],[7,8,12,13,66,99],[3,2,55,66,78,99]])
print(np1[0:4,3])

#Returns the elements at indices 0,1
import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
print(np1[:2])

#Returns the elements at index 1 on all rows
import numpy as np
np1=np.array([[1,2,3,4,9,6],[5,6,10,11,76,4],[7,8,12,13,66,99],[3,2,55,66,78,99]])
print(np1[:,1])