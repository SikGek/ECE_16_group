import numpy as np
a = np.array([1, 2, 3])
a = np.array([(1,2,3),(4,5,6)])
a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
myList = [1,2,9,8]
a = np.array(myList)
a = np.zeros((2,2))
a = np.ones((3,3))
a = np.array([(1,2,3),(4,5,6)])
a.reshape(3,2)
a = np.array([(1,2,3),(4,5,6)])
b = a.flatten()
b.shape # (6,) NOT (6,1)!
a = np.array([1,2,3,4,5,6,7])
b = np.resize(a, (1,4)) # array([[1, 2, 3, 4]])
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.hstack((a,b))
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))

a = np.arange(1,11,1)
a = np.linspace(1.0,5.0,10, False)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a[0] # This gives us the first row of a
a[2] # This gives us the third row of a
a[:,1] # this gives us the second column of a
a[2][2] # this gives us the value of a(2,2), which is 9 here

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = a[1] # This gives us the 2nd row of a ([4,5,6])
c[2] = 0 # This assigns the 3rd element to 0 in c, but ALSO in a!
a        # [[1,2,3],[4,5,0],[7,8,9]] – NOTICE THE ZERO!!!

array1 = np.array([0,10,4,12])
array1_0 = array1 - 20
print(array1_0) #array1 is a simple 1d array with values: [-20 -10 -6 -8], since it subtracted 20 from all original values
array2 = np.array([[0,10,4,12],[1,20,3,41]])
array2_new = np.array([[array2[0,2:]],[array2[1,:2]]])
print(array2_new) #I created a new array with specific indexes required from the original array
array1_2 = np.hstack((array1,array1))
array3 = np.vstack((array1_2,array1_2,array1_2,array1_2))
print(array3)
array4a = np.arange(-3,18,6)
array4b = np.arange(-7,-21,-2)
print(array4a,"\n",array4b)
array5 = np.linspace(0,100,49)
print(array5) #this differs from arange as this focuses on the number of elements within an array to create the array, as opposed to arange which focuses on the increments. You might use linspace over arange when you need an evenly spaced array of a specific size and you don't want to do the calculation
array6 = np.zeros((3,4))
array6[0] = [12,3,1,2]
array6[2,2] = 2
array6[2,0:2] = [4,2]
array6[2,2:] = array6[0,1:2]
array6[2,3] = array6[0][2]
array6[:,2] = [1,1,3]
array6[1,3] = 2
print(array6)
print(array6[0])     # [12 3 1 2]
print(array6[1, 0])  # 0
print(array6[:, 1])  # [3 0 2]
print(array6[2, :2]) # [4 2]
print(array6[2, 2:]) # [3 1] 
print(array6[:, 2])  # [1 1 3]
print(array6[1, 3])  # 2
string7 = '1,2,3,4'
array7_1 = np.zeros(4)
q = 0
for x in range(7):
    if string7[x] != ',':
        array7_1[q] = int(string7[x])
        q += 1
array7 = array7_1[:]
for x in range(99):
    array7 = np.vstack((array7, array7_1))
print(array7)