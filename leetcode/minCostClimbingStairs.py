# https://leetcode.com/problems/min-cost-climbing-stairs/description/


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        replace each step with the cumulative cost (min)
        compare it with 1 step and 2 step
        20 -> cannot compare, so it will be 20
        15 -> 20+15, 15. so it will be 15
        10 -> 10+15, 25. 10 + 20 -> 30
        0 -> 30, 15
        1,100,1,1,1,100,1,1,100,1
        6,105,5,5,4,102,3,2,100,1
        """

        pointer = len(cost) - 1

        while pointer >= 0:
            if pointer + 2 < len(cost):
                cost[pointer] += min(cost[pointer + 1], cost[pointer + 2])
            elif pointer + 1 < len(cost):
                cost[pointer] = min(cost[pointer], cost[pointer + 1] + cost[pointer])
            pointer -= 1

        return min(cost[0], cost[1])
