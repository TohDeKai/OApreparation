# https://leetcode.com/problems/kth-distinct-string-in-an-array/?envType=daily-question&envId=2024-08-05


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        BRUTE FORCE O(N^2)
        iterate through the whole list to find out if it is distinct
        if distinct, add 1 to count
        when count = k, return string

        optimised - O(N) time n space
        have a set
        run a loop through twice, first to add it to the set
        second to check if its distinct
        """
        count = {}
        for elem in arr:
            if elem not in count:
                count[elem] = 1
            else:
                count[elem] += 1

        num_distinct = 0
        for elem in arr:
            if elem in count and count[elem] == 1:
                num_distinct += 1
            if num_distinct == k:
                return elem

        return ""
