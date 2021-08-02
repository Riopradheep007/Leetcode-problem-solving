



def canPlaceFlowers(flowerbed,n):
     size=len(flowerbed)
     new=[0]+flowerbed+[0]
     for i in range(1,size+1):
          if new[i]==new[i-1]==new[i+1]==0:
              new[i]=1
              n-=1
          if n<=0: return True
     return False
canPlaceFlowers([1,0,0,0,1],1)
        

