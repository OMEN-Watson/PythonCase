# a_list = [1,3,2,4]
# print(a_list)
# a_list[1:3]=[-1,-2]
# print(a_list)
import copy
row1=["H","He"]
row2=["Li","Be","B","C","N","O","F","Ar"]
row3=["Na","Mg","Al","Si","P","S","Cl","Ne"]
# ptable=row1[:]
# ptable=row1
# ptable=[row1]
# ptable.append(row2)
# print(ptable)
# print(row1)
ptable1=["H","Xe",row2]

ptable2=copy.deepcopy(ptable1)
# print('-----')
# print('ptable1:')
# print(  ptable1)
# print('ptable2:')
# print(ptable2)
# ptable2[2][7]='Ne???'
# print('NEW-ptable1:')
# print( ptable1)
# print('NEW-ptable2:')
# print( ptable2)
# print(id(ptable1))
# print(id(ptable2))
# print(id(ptable1[2]))
# print(id(ptable2[2]))
# print(help(list.append))
# listTest=[1,2,3,4]
# print(listTest)
 
# print(print(tupleTest[0:2])) 
# tupleTest2=1,2,3,4
# print(type( tupleTest2))
# tupleTest3=()
# tupleTest4=()
# print(type( tupleTest3))
# print(type( tupleTest4))
# listTest.pop(0)
# print(listTest)
import random
def perfect_shuffle_in_place(aList):
  newList=list()
  while(len(aList)>0):
    newIndex=random.randrange(len(aList))
    newList.append(aList[newIndex])
    del aList[newIndex]
  for oneNum in range(len(newList)):
    aList.append(newList[oneNum])

my_list = [1, 2, 3, 4, 5, 6]
perfect_shuffle_in_place(my_list)
print(my_list)