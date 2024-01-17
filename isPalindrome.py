class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        brute force
        reverse string, remove whitespaces, check if it is same as unreversed string
        O(n) space and time

        optimised
        2 pointers left (l) and right(r)
        l starts from left, moving towards right and r starts from right, moving towards l
        check if elem at l and r pointer are same
        O(n) time, O(1) space
        """
        l, r = 0, len(s) - 1
        while l < r:
            # to skip over non alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True
