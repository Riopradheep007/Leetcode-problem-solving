
     Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

def generate( numRows):
    result = []
    row = [1]
    for j in range(numRows):
        result.append(row)
        row=generateNextRow(row)
    return result  
def generateNextRow(prevRow):
    nextrow = []
    nextrow.append(1)
    for i in range(len(prevRow)-1):
        sumTwoEle = prevRow[i]+prevRow[i+1]
        nextrow.append(sumTwoEle)
    nextrow.append(1)
    return nextrow
n=int(input())
print(generate(n))
