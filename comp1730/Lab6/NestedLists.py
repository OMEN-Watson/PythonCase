def countDepth(oneList):
  result=0
  for i in oneList:
    max(result, subMethod(i)    )

def subMethod(subList):
  if(type(subList) is int):
    return 0
  elif(type(subList) is list):
    result=0  
    for i in subList:
      depth=subMethod(i)
      result=max(result,depth    )
    return result+1
  
    
    

print( '--------')
anyOne=[[1,2], [2,4]]
anyOne=[[1,[2]],3]
anyOne=[1, [2], [[3], [[4], 5]]]
anyOne=[[[]]]
print( subMethod(anyOne)-1)
