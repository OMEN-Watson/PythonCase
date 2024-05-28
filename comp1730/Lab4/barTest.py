import matplotlib.pyplot as plt
import numpy as np
# def count_in_bin(values,lower,upper):




# binsData.sort
# box= [[] for i in range( len(binsData)+1)]
# for bIndex in range(len(binsData)) :
#   border = binsData[bIndex]
#   rIndex=0
#   while (rIndex<len(resource)):
#     crtNumber=resource[rIndex]
#     if crtNumber<=border:
#       box[bIndex].append(crtNumber)
#       resource.remove(crtNumber)
#     else :
#       rIndex+=1
# if(len(resource)>0):
#   box[len(box)-1].extend(resource)
# fig, ax = plt.subplots()
# fruits = []

# for botText in binsData:
#   fruits.append(str(botText))
# strLastOne=">"+str(binsData[len(binsData)-1])
# fruits.append(strLastOne)
# counts = []
# for oneList in box:
#   counts.append(len(oneList))
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']

# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
# ax.bar(fruits, counts  )
# # ax.set_ylabel('fruit supply')
# # ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')

# plt.show()
def count_in_bin(values,dividers):
  resource=values
  binsData=dividers
  binsData.sort
  box= [[] for i in range( len(binsData)+1)]
  for bIndex in range(len(binsData)) :
    border = binsData[bIndex]
    rIndex=0
    while (rIndex<len(resource)):
      crtNumber=resource[rIndex]
      if crtNumber<=border:
        box[bIndex].append(crtNumber)
        resource.remove(crtNumber)
      else :
        rIndex+=1
  if(len(resource)>0):
    box[len(box)-1].extend(resource)
  fig, ax = plt.subplots()
  fruits = []
  for botText in binsData:
    fruits.append(str(botText))
    strLastOne=">"+str(binsData[len(binsData)-1])
  fruits.append(strLastOne)
  counts = []
  for oneList in box:
    counts.append(len(oneList))
  ax.bar(fruits, counts  )
  plt.show()

resource=[i+1 for i in range(10)]
binsData=[2,5,7]
# count_in_bin(resource,binsData)
resource=[2.09, 0.5, 3.48, 1.44, 5.2, 2.86, 2.62, 6.31]
binsData=[0,2,4,7]

xdata=np.array(resource)
xbins=np.array(binsData)

fig, ax = plt.subplots()
ax.hist(xdata,xbins)
ax.plot(xdata, 0*xdata, 'd')
plt.show()