# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        create a hashmap to keep count
        have a l and r pointer
        keep r going, as long as the character does not exist in hashmap or count = 0
        add 1 to the hashmap with the character at r as a key
        when repeat, move l and minus 1 with character at l as a key
        keep count of the length, update the longest length captured
        """
        l = r = 0
        count = {}
        res = 0
        while r < len(s):
            if s[r] not in count or count[s[r]] == 0:
                count[s[r]] = 1
                res = max(res, r - l + 1)
                r += 1
            else:
                count[s[l]] = 0
                l += 1
        return res
