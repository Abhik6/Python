# Best time to buy and sell stock
# Asked in Companies:

# Apple
# Myntra
# Media.net
# Facebook


# Description:
# You are given an integer array prices where prices[i] represents the price of a given stock on the i-th day.
# On each day, you may decide to buy and/or sell the stock. However, you can only hold at most one share of the stock at any time. You can also buy and then immediately sell the stock on the same day.
# Find and return the maximum profit you can achieve.


# Input Parameters:
# prices (List[int]): An array representing the prices of the stock on each day.

# Output:
# Return an integer representing the maximum profit you can achieve.


# Example:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#              Total profit is 4 + 3 = 7.
 
 
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Total profit is 4.
 
 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make any profit, so we return 0.


def maxProfit(prices):
    """
    Function to return the maximum profit you can achieve by buying and selling stocks.
    
    :param prices: List[int] -> List of stock prices per day
    :return: int -> Maximum profit
    """

    n = len(prices)
    buy = prices[0]
    sell = prices[0]
    profit = [0]*n

    for i in range(1,n):
        if prices[i] > prices[i-1]:
            sell = prices[i]
            if i == n-1:
                sell = prices[i]
                profit[i] = sell - buy
        else:
            profit[i-1] = sell - buy
            buy = prices[i]
            sell = prices[i]
    
    result = sum(profit)

    return result

# prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
print(maxProfit(prices))


## Another Implementation

def maxProfit(prices):
    """
    Function to return the maximum profit you can achieve by buying and selling stocks.
    
    :param prices: List[int] -> List of stock prices per day
    :return: int -> Maximum profit
    """
    # Initialize the maximum profit to 0
    max_profit = 0
    
    # Traverse through the prices starting from the second day
    for i in range(1, len(prices)):
        # If the price of the current day is higher than the previous day
        # Add the difference to the maximum profit (this simulates buying on the previous day and selling today)
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    
    return max_profit
    
            
