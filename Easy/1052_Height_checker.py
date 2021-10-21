                       ##################################################################################################33
                                                                Height Checker
                       ####################################################################################################
"""
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

"""

Time complixity is O(n logn)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        orderedHeights = sorted(heights)
        size = len(heights)
        for i in range(size):
            if orderedHeights[i] != heights[i]:
                count += 1
        return count

time complixity is O(n)

import collections
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = collections.Counter(heights)
        i = 0

        removals = 0
        for height in heights:
            while counter[i] == 0:
                i += 1

            if i != height:
                removals += 1

            counter[i] -= 1


        return removals
                
                
