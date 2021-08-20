   You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.




def maxProfit(prices):
    minPrice = prices[0]
    maxPrice = 0
    profit = 0
    totalProfit = 0
    
    for price  in prices[1:]:
        if minPrice > price:
            minPrice = price
            
        if price - minPrice > 0:
            maxPrice = price
            profit = maxPrice - minPrice
            totalProfit += profit 
            minPrice = price
            maxPrice = 0
    return totalProfit
list_of_prices=list(map(int,input().split()))
print(maxProfit(list_of_prices))
