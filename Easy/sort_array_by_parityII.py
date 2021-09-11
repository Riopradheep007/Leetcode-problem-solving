


    Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odd = []
        even = []

        for i in  nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
                
        result = []
        for i in  range(len(even)):
            result.append(even[i])
            result.append(odd[i])
        return result


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(nums)

        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                nums[i],nums[j] = nums[j],nums[i]
                i += 2
                j += 2

        return nums
