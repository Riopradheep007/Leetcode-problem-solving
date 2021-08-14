"""
   Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]

""" 
def plusOne(digit):
	size=len(digit)
	digit[size-1] += 1
	carry = digit[size-1]/10
	digit[size-1] = digit[size-1]%10

	for element in range(size-2,-1,-1):
	    if carry==1:
		digit[element] += 1
		carry = digit[element]/10
		digit[element] = digit[element]%10
		
	if carry == 1:
	    digit.insert(0,1)
	return digit

digit = list(map(int,input().split()))
print(plusOne(digit))
