import numpy as np
A= np.array([
[0.0,12.0,-1.0,5.0],
[-1.0,-1.0,-1.0,0.0],
[11.0,5.0,5.0,-2.0]
]
)


# rr=range(0,10)
# for i in rr:
#   print (i)

# for i in range(0,A.shape[0]):
#   for j in range(0,A.shape[1]):
#     print("A["+str(i)+","+str(j)+"]="+str(A[i,j]))

# print(A[0,:])

# print(A[1:3,1:3])

DirectionArray=np.array([
        [-1,-1],
         [-1,0],
          [-1,1],
           [0,1],
            [1,1],
             [1,0],
              [1,-1],
               [0,-1]
    ])
oneCoordinate=np.array([3,3])

DirectionArray=DirectionArray+oneCoordinate

print(DirectionArray)