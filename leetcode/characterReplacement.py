# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        have 2 pointers l and r and counter
        if s[r] != s[l], counter++
        if counter > k: start moving l,
        if s[l] != s[r], counter --
        '''