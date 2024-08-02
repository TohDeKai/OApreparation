# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/


class Solution:
    def numSplits(self, s: str) -> int:
        """
        create hashmap count of letters
        while iterating, count unique letters
        that number will be assigned to unique_right
        unique_left will start at 0

        create new hashmap
        with a pointer
        if letter[pointer] not in new hashmap, unique_left +1
        hm[letter[pointer]] - 1 -> if updated to be 0, unique_right -1

        when unique_left == unique_right, res +1
        """
        res = 0
        hm = {}

        unique_right = unique_left = 0
        pointer = 0
        while pointer < len(s):
            if s[pointer] not in hm:
                hm[s[pointer]] = 1
                unique_right += 1
            else:
                hm[s[pointer]] += 1
            pointer += 1

        pointer = 0
        hm_left = {}

        while pointer < len(s):
            if s[pointer] not in hm_left:
                hm_left[s[pointer]] = 1
                unique_left += 1

            hm[s[pointer]] -= 1
            if hm[s[pointer]] == 0:
                unique_right -= 1

            if unique_left == unique_right:
                res += 1
            pointer += 1

        return res
