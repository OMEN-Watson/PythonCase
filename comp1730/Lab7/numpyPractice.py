import numpy as np
import math
import doctest
import unittest


 

 
 
x = np.array([0.0, 0.25, 0.5, 0.75, 1.0])


# print (type(x))
# y=np.zeros(5)
# print (y)
# z=np.linspace(0.0,10.0,5)
# print (z)
# print (type(z))
# t = np.arange(0.0, 5.0, 0.5)
# print (t)
# help(np.zeros)
def  testDouble(x):
  return x*2
y=np.zeros(10)
y[0]=0.0
y[1]=0.01
y[2]=0.02
y[3]=0.03
print (y[1:-2])
x = np.linspace(0.0, 20, 10)
print (x)
print(np.sin(x))
# print( math.sin(x))
print(testDouble(x))
hh=19
# print(type(hh) is int)
# assert type(hh) is [],"hahaNo!"
# print( unittest.TestCase.assertTrue(type(hh) is int,"this is message"))
# print( unittest.TestCase.assertTrue('hello'.isupper(),'edede'))

# print( unittest.TestCase.assertFalse(type(hh) is int,"this is message"))

# unittest.TestCase.assertIs(type(hh),int,'tete' ) 
import matplotlib.pyplot as plt

plt.plot(x,y)
plt.grid()
plt.show()