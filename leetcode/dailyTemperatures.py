# https://leetcode.com/problems/daily-temperatures/description/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        BRUTE FORCE APPROACH
        for every element i, iterate through the rest of the list to find the next highest temp, then calculate the number of days
        O(n^2)

        5 3 6
          ^

        we want to keep a stack of the elements for as long as it is decreasing

        for each element,
        pop the stack, check if it is bigger
        if it is bigger, just compare the diff in index and add it to result
        --> how do we do the tracking of index and temperature?
        --> for the stack, we append(temp, idx)

        we will iterate through the whole list
        for any thing left in the stack, we will just append 0

        30 60 90

        [(60,1)]
        [1,1,0]
        """
        res = [0] * len(temperatures)
        stack = []

        pointer = 0

        while pointer < len(temperatures):
            while stack and stack[-1][0] < temperatures[pointer]:
                res[stack[-1][1]] = pointer - stack[-1][1]
                stack.pop()

            stack.append((temperatures[pointer], pointer))
            pointer += 1

        return res
