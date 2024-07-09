# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Have a hashmap that keeps count of the occurrence of the number of character within the sliding window
        Keep track of which is most frequent character in sliding window
        For right pointer, if character is the most freq character, cont moving
        If not, check if len(sliding window) - count[most freq] > k.
            if it is, then move l until that is untrue
        everytime R moves, compare max(res, len(sliding window))
        """
        l = r = res = 0
        n = len(s)
        count = {}
        most_freq = s[0]
        while r < n:
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l + 1) - count[most_freq] > k:
                count[s[l]] -= 1
                l += 1
                if count[s[l]] >= count[most_freq]:
                    most_freq = s[l]
            if count[s[r]] >= count[most_freq]:
                most_freq = s[r]
            res = max(res, r - l + 1)
            r += 1
        return res
