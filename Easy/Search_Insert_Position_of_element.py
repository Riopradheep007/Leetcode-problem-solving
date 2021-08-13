   
	Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1



def searchInsert(nums,target):

	size=len(nums)
	for i in range(0,size):
	    if nums[i]==target:
		return i
	    elif nums[i]>target:
		return i
	return size
print(searchInsert([1,3,5,6],5))
