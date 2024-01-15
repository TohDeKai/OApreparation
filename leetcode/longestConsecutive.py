# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        In order to have a O(n), it will be a solution that keeps track of the occurrence of the number.
        We will have to consider what exactly we want to keep track of.
        Number of occurrence? - no, that's not relevant to consecutive
        to find consecutive, we want to know whether the number +1 or -1 exists
        since we are finding longest consec, we don't need to care about duplicates
        we can use a set data structure to have O(1) find operation
        let longest = 1
        for every elem, we try and found a longest sequence if it is the start of the sequence
        for every elem i, we check if i-1 exists. O(1) time
        if does not exist, we check if i+1 exists, and then we continue until i+1 does not exist.
        we check if length of sequence is higher than longest. let longest be the bigger number of the two
        return longest

        since we go through every element at most twice,
        time complexity O(n)
        space complexity O(n) because need to form the set
        """

        nums = set(nums)
        longest = 0

        for num in nums:
            # if start of a sequence
            if num - 1 not in nums:
                # extending sequence
                sequence = num + 1
                while sequence in nums:
                    sequence += 1
                # when sequence is done, update longest count if sequence is longer than previous longest sequence
                longest = max(longest, sequence - num)

        return longest
