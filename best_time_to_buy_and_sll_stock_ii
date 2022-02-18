# Best Time to Buy and Sell Stock II
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        if len(prices) > 1:
            for i in range(0, len(prices)-1):
                if prices[i] < prices[i+1]:
                    profit -= prices[i]
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i]
        return profit
