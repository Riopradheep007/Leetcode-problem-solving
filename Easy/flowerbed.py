

'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.


eg1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

eg2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''

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
        

