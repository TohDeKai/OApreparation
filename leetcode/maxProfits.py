# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        I want to find max profits

        In order to do that - I need to buy low sell high
        the day where I sell needs to be after the day I buy

        Brute Force Approach
        for each day, I buy on that day
            Iterate through the rest of the days, and take it as I sell them
            Compare the profits to find maximum - Find profit by taking price[sell] - price[buy]
        If profit is negative, return 0. Else return profits
        O(n^2) time complexity

        [a,b,c,d,e,f,g,h]
        ^buy
        ^sell
                ^buy
                ^sell

        Optimised Solution
        Have a single pointer, and a buy and sell pointer. Have a max_profit and curr_profit counter.]
        Set pointers and counters at 0.
        When prices[pointer] is lower than prices[buy], set buy to pointer. Set sell to pointer too.
        When prices[pointer] is higher than prices[sell], set sell to pointer.
        If buy =/= sell, set max_profit to curr_profit if it is bigger than max_profit.
        After you finish iterating, if max_profit is less than 0, return 0. Else, return max_profit
        O(n)
        """
        pointer, buy, sell, n = 0, 0, 0, len(prices)
        max_profit, curr_profit = 0, 0
        if n == 1:
            return 0

        while pointer < n:
            if prices[buy] > prices[pointer]:
                buy = pointer
                sell = pointer
            if prices[sell] < prices[pointer]:
                sell = pointer
            if buy != sell:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, curr_profit)
            pointer += 1

        return max(0, max_profit)
