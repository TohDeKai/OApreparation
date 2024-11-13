# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Start at the back
        Compare with 1 step in front and 2 step to decide which to take
        Take the smaller one and add it to the cumulative cost
        At the end, take minimum of 1 step or 2 step
        """

        n = len(cost)
        pointer = n - 1

        while pointer >= 0:
            if pointer + 2 < n:
                cost[pointer] += min(cost[pointer+1],cost[pointer+2])
            pointer -= 1 
        
        return min(cost[0],cost[1])