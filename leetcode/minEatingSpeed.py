# https://leetcode.com/problems/koko-eating-bananas/description/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        brute force
        take every value of k until it matches h
        o(n^2)

        find max value of piles
        0 < k < max(piles)
        use binary search to find the match
        O(nlog(max(piles)))
        """
        max_p = max(piles)
        res = max_p
        l, r = 1, max_p

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1

        return res
