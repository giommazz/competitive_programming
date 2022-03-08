"""
Best Time to Buy and Sell Stock II (LeetCode)

found at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""

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
