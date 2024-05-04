row1=["H","He"]
row2=["Li","Be","B","C","N","O","F","Ar"]
row3=["Na","Mg","Al","Si","P","S","Cl","Ne"]
# ptable=row1
# print(ptable)
# ptable.extend(row2)
# print(ptable)
# ptable.extend(row3)
# print(ptable)
# print(row1)
# print(row2)
# row2[7]='Neeeee'
# print( row2)
# print(ptable)
# print(row3)
# ptable[17]='Arrrrr'
# print(ptable)
# print(row3)

ptable=[row1]
# ptable=row1
print(ptable)
ptable.append(row2)
print(ptable)
ptable.append(row3)
print(ptable)
print(row1)
print(row2)

print( ptable[1][5])
print( ptable[2][1])
row2[len(row2)-1]='Neeeee'
print(row2  )
row3[len(row3)-1]='Arrrrr'
print( row3 )
print(ptable)