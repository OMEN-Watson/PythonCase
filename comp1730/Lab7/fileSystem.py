import os
print('-----')
# print( os.getcwd())
# os.getcwd()
# os.chdir('D:\\01Gan\\abroad\\study\\05ANU\\ProgrammingForScientists\\PythonCase\\comp1730\\lab7')

# os.chdir('Lab7')
# print( os.getcwd())
# os.chdir('..')
# os.chdir('..')
# print( os.getcwd())
# # print(os.listdir('D:\\01Gan\\abroad\\study\\05ANU\\ProgrammingForScientists\\PythonCase\\comp1730\\Lab7'))
# print(os.listdir('..'))
# print(os.getcwd())

os.chdir('lab7')
print('-----')
fileobj=open('daily-max-temp-CBR.csv','r')
# strList=['jay zhou\n','JJ Lin','FanYue']
# fileobj.writelines(strList)
# for oneLine in fileobj:
#   print(oneLine)
# print(fileobj.tell())
print( fileobj.readline())
print(fileobj.tell())

print( fileobj.readline())
print(fileobj.tell())
# fileobj.seek(22)
print( fileobj.readline())
print( fileobj.readline())
# print( type( fileobj.readline()) )
fileobj.close()