# https://leetcode.com/problems/minimum-window-substring/


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Create hashmap of letters in t
        Let N be len(t)
        have res
        have left and right pointer
        if s[r] in hm, hm[s[r]] - 1 and N - 1
        if N == 0:
            res = s[l:r] if l:r < len(res)
        move l
            if s[l] in hm:
                hm[s[l]] + 1 and N + 1
                then continue with R
            else
                move and update res
        """
        hm = {}
        for char in t:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1
        res = s
        l, r = 0, 0
        n = len(t)
        valid = False
        while r < len(s):
            if s[r] in hm:
                if hm[s[r]] > 0:
                    n -= 1
                hm[s[r]] -= 1

            while n == 0:
                valid = True
                if r - l + 1 < len(res):
                    res = s[l : r + 1]

                if s[l] in hm:
                    hm[s[l]] += 1
                    if hm[s[l]] > 0:
                        n += 1
                l += 1
            r += 1

        if valid:
            return res
        else:
            return ""
