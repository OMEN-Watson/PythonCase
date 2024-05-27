
def  fn2(d):
  newd=d.copy()
  newd['test']=2
  return newd

d=dict()
print(d)
print()
dd=fn2(d)
print(d)