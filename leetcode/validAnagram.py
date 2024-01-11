# https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Create a hashmap to keep count of occurrence of each letter within s
        Iterate through t
        Check if element is within hashmap, and if it is, if it's above 0
        then minus off the count to keep track.
        If it's below 0 or element not within hashmap, return false
        if iterate through whole of t, return true

        O(n) time and space complexity
        """

        # creating hashmap
        count = {}

        # iterating through s to populate the count
        pointer, n = 0, len(s)

        # if not equal length, no way to be a valid anagram
        if n != len(t):
            return False

        while pointer < n:
            if s[pointer] not in count:
                count[s[pointer]] = 1
            else:
                count[s[pointer]] += 1
            pointer += 1

        # resetting pointer to iterate through t
        pointer = 0

        while pointer < n:
            if t[pointer] not in count:
                return False
            else:
                if count[t[pointer]] == 0:
                    return False
                else:
                    count[t[pointer]] -= 1
                pointer += 1

        return True
