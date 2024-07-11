# https://leetcode.com/problems/compare-version-numbers/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # a solution that takes O(1) space complexity
        pointer1 = pointer2 = count1 = count2 = 0
        leading_zeros_1 = leading_zeros_2 = True
        while pointer1 < len(version1) or pointer2 < len(version2):
            while pointer1 < len(version1) and version1[pointer1] != ".":
                count1 += int(version1[pointer1]) + 10 * count1
                pointer1 += 1
            while pointer2 < len(version2) and version2[pointer2] != ".":
                count2 += int(version2[pointer2]) + 10 * count2
                pointer2 += 1

            if count1 < count2:
                return -1
            elif count1 > count2:
                return 1
            else:
                pointer1 += 1
                pointer2 += 1
                count1 = count2 = 0

        return 0
