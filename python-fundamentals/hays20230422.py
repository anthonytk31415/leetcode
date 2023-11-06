def removeDupesFrom2(arr1, arr2):
  arr1Check = set(arr1)
  arr2Check = set(arr2)
  
  res1 = []
  for x in arr1: 
    if x not in arr2Check:
      res1.append(x)
  
  res2 = []	
  for x in arr2:
    if x not in arr1Check:
      res2.append(x)
  
  return res1, res2

arr1 = [1,2,3]
arr2 = [4,5,3]

print(removeDupesFrom2(arr1, arr2))





ñ