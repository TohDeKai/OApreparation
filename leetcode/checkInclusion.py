# https://leetcode.com/problems/permutation-in-string/description/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        create an array of size 26 -> idx correspond to letter and number of occurrence
        compare both array everytime. it's O(1) 26 times
        """
        s1_count = [0] * 26
        s2_count = [0] * 26

        if len(s1) > len(s2):
            return False

        for char in s1:
            s1_count[ord(char) - ord("a")] += 1

        r = 0
        while r < len(s1):
            s2_count[ord(s2[r]) - ord("a")] += 1
            r += 1

        l = 0
        while r < len(s2):
            if s2_count == s1_count:
                return True
            s2_count[ord(s2[r]) - ord("a")] += 1
            r += 1
            s2_count[ord(s2[l]) - ord("a")] -= 1
            l += 1

        return s2_count == s1_count
