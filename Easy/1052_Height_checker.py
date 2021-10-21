
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
                
                
