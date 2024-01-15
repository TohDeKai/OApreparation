# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Brute force approach:
        Create a copy of the nums list
        For every element in the list, iterate through every other element in the copied list and replace it with the multiple
        O(n^2) time complexity O(n) space

        Optimised:
        [a,b,c,d] -> nums
        [a, ab, abc, abcd]-> cumulative multiplication forward
        [abcd, bcd, cd, d]-> cumulative multiplication backwards
        [bcd, acd, abd, abc] -> res

        noticing pattern
        for element i in res, it is i - 1 in the forward multiplication * i + 1 in the backwards multiplication

        hence
        create 3 list, forwards, backwards, res
        iterate through forwards and form cumulative multiplication
        do the same for backwards but do it from the back
        iterate for number of elements in num
        take backwards[i+1] * forwards[i-1] if it exists. otherwise just take one of them

        O(n) time complexity
        """
        forwards, backwards, res = [], [], []
        for num in nums:
            forwards.append(num)
            backwards.append(num)
        pointer, n = 1, len(nums)

        while pointer < n:
            forwards[pointer] = forwards[pointer] * forwards[pointer - 1]
            backwards[n - pointer - 1] = (
                backwards[n - pointer - 1] * backwards[n - pointer]
            )
            pointer += 1

        for i in range(n):
            prod = 1
            if i != 0:
                prod *= forwards[i - 1]
            if i != n - 1:
                prod *= backwards[i + 1]
            res.append(prod)

        return res
