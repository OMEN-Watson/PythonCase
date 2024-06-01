import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('Lab9')

    # create the image array (fill with 0s)
# image[0,0,:] = 1.0, 0.0, 0.0  # RGB for top-left (0,0) pixel
# image[0,1,:] = 0.0, 1.0, 0.0  # RGB for top-middle (1,0) pixel
# image[0,2,:] = 0.0, 0.0, 1.0  # RGB for top-right (2,0) pixel
# image[1,0,:] = 1.0, 1.0, 0.0  # RGB for row 2 left (0,1) pixel
# image[1,1,:] = 1.0, 1.0, 1.0  # RGB for row 2 middle (1,1) pixel
# image[1,2,:] = 0.0, 0.0, 0.0  # RGB for row 2 right (2,1) pixel

f=open("cat_picture_1.ppm",'r')
print(f.readline())
widthAndHeight= f.readline()
width=int( widthAndHeight.split(' ')[0])
height=int( widthAndHeight.split(' ')[1])
print(width)
print(height)
image = np.zeros((width,height,3)) 
maxColor=int( f.readline())

crtStr=f.readline()
rowNum=0
colNum=0
while  crtStr.endswith('\n')>0:
  crtStr=crtStr[:len(crtStr)-1]
  if( len(crtStr)==0):
    break
  allColorsInOneLine=crtStr.split(' ')
  for i in range(0,len(allColorsInOneLine),4):
    fstStr=allColorsInOneLine[i]
    sndStr=allColorsInOneLine[i+1]
    trdStr= allColorsInOneLine[i+2]
    fstEle= int( fstStr)/maxColor
    sndEle= int( sndStr)/maxColor
    trdEle= int( trdStr)/maxColor

    image[rowNum,colNum,:]=fstEle,sndEle,trdEle
    colNum=(colNum+1)%height
    if(colNum==0):
      rowNum+=1
  crtStr=f.readline()
  print(rowNum)
  print(colNum)
  print(crtStr)
  # rowNum+=1
plt.imshow(image, interpolation='none')
plt.show()
f.close()