"""             
                                 ###################################3##########################################
                                                                   Range Addition
                                 ##############################################################################
   You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

 

Example 1:


Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
Example 3:

Input: m = 3, n = 3, ops = []
Output: 9

"""


'''
  First i wrote this code straight forward appeoah but some of the test case not passed 
  
  Memory limit ezceed
'''

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        ls=[[0]*m for i in range(n)]


        max_ele = 0

        for i in ops:
            val = i[0]
            for i in range(val):   
                for j in range(val):
                    ls[i][j] += 1 
                if max_ele < max(ls[0]):
                    max_ele = max(ls[0])

        count = 0
        for i in range(len(ls)):
            count += ls[i].count(max_ele)
        
        return count


"""
 The be;;pw code works fine
"""
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        x,y = zip(*ops)
        return min(x) *  min(y)
