def merge(arr1,arr2):
   d=[]
   y=0
   z=0
   while(y<len(arr1) and z<len(arr2)):
      if(arr1[y]<arr2[z]):
         d.append(arr1[y])
         y+=1
      else:
         d.append(arr2[z])
         z+=1
   while(y<len(arr1)):
      d.append(arr1[y])
      y+=1
   while(z<len(arr2)):
      d.append(arr2[z])
      z+=1
   return d

def mergesort(array):
   if(len(array)==1):
      return array
   mid=(len(array))//2
   arr1=mergesort(array[:mid])
   arr2=mergesort(array[mid:])
   return merge(arr1,arr2)
array=[2,1,8,6,3,9,11,12,45,18]
print(mergesort(array))



