# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
 
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        coin_count = []
        for coin in coins:
            # print(f"Coin : {coin}")
            rem_amount = amount - coin
            # print(f"Remaining Amount : {rem_amount}")
            coin_count.append(self.coinChange(coins, rem_amount))
            # coin_count = min(coin_count, self.coinChange(coins, rem_amount))
        if all(map(lambda x: True if x<0 else False, coin_count)):
            min_count = -1
        else:
            min_count = min([count for count in coin_count if count>=0])
         
        return (1 + min_count) if min_count>=0 else -1

    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        memo = {}
        return self.coinChange_memo_helper(coins, amount, memo)

    def coinChange_memo_helper(self, coins: List[int], amount: int, memo: dict) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        coin_count = []
        for coin in coins:
            # print(f"Coin : {coin}")
            rem_amount = amount - coin
            if rem_amount in memo:
                coin_count.append(memo[rem_amount])
            else:
                # print(f"Remaining Amount : {rem_amount}")
                count = self.coinChange(coins, rem_amount)
                coin_count.append(count)
                memo[rem_amount] = count
            # coin_count = min(coin_count, self.coinChange(coins, rem_amount))
        if all(map(lambda x: True if x<0 else False, coin_count)):
            min_count = -1
        else:
            min_count = min([count for count in coin_count if count>=0])
        
        return (1 + min_count) if min_count>=0 else -1
        
    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        # print(len(dp))

        for i in range(1, amount+1):
            # print(i)
            for c in coins:
                 if i-c>=0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if dp[amount]!=(amount+1) else -1










    # def coinChange(self, coins: List[int], amount: int) -> int:

    #     sum =  0
    #     count = 0

    #     while sum < amount:
    #         if sum == amount:
    #             break
    #         if sum == -1:
    #             return sum
    #         coins_sum = [sum + coin for coin in coins]
    #         sum = max([elem for elem in coins_sum if elem<=amount] + [-1])
    #         print(sum)
    #         count+=1
    #         print(count)
    #     return count

    # def coinChange2(self, coins: List[int], amount: int) -> int:

    #     def coinChange_helper(coins, amount, sum):
    #         sum+=coin
    #         if sum == amount:
    #             return 1
    #         min_coins = 0
    #         for coin in coins:
    #             min_coins = min(min_coins, coinChange_helper(coin, amount, sum))
    #         return coinChange_helper()



# coins = [1,2,5] 
# amount = 11
# coins = [2] 
# amount = 3
# coins = [1] 
# amount = 0
coins = [186,419,83,408]
amount = 6249
sol = Solution()
# result = sol.coinChange(coins, amount)
# print(result)
# result2 = sol.coinChange_memo(coins, amount)
# print(result2)
result3 = sol.coinChange_dp(coins, amount)
print(result3)