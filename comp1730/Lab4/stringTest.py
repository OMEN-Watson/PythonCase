
testStr="The possessive form of 'it' is 'its'."
testStr="\"It's\" is an abbreviation of \"it is\"."
testStr="A ''' is three ' but two ' do not make a \""
testStr='''i have 
three line
nice wow'''
testStr="i use '\\n'\n in this str"
# print(testStr)

# print( ord('a'))
# print( ord('A'))
# print( chr(97))
# print( chr(91))
# print( chr(92))
# print( chr(93))
# print(chr(20986)+chr(21475))

# print(chr(5798)+chr(5794)+chr(5809)+chr(5835)+chr(5840)+chr(5830)+chr(5825)+chr(5823))

aseq="abcd"
print( type(aseq))
print(aseq+aseq)
print(aseq*4)
print(aseq[0])
print(type(aseq[0]))
print( aseq[-2])
print(aseq[1:-2])
print(aseq[1:2])
bseq="adbc"
print(aseq<bseq)
for elem in aseq:
  print (elem)

print( min(aseq))
print(max(aseq))
print(sorted(aseq))

aseq=[1,2,3,4]
bseq=[1,3,2,4]
print( type(aseq))
empty=[]
print(sorted(empty))
# print(min(empty))
# print(max(empty))
abLol="123456789"
# for a,b in abLol:
#   print('a is {} and b is {}').__format__(a,b)

my_list = [i  for i in range(26)]
print(my_list)
sentence = "the COMP1730 lectures are boring, but the labs are great"
print(sentence.title())