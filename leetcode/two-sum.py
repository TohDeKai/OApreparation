# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force
        For every element in the list, go through the rest of the list to find target - element.
        O(n^2)

        Optimised
        Have a hashmap to keep count of the occurrence of the elements
        For each element, add the element as a key and indice as a value to the hashmap
        Check if target - element exists in hashmap
        O(n) time and space
        """

        # creating hashmap
        count = {}

        # iterating through list
        pointer, n = 0, len(nums)

        while pointer < n:
            # if element not in hashmap, add to hashmap with key-value pair being element and indice respectively
            if nums[pointer] not in count:
                count[nums[pointer]] = pointer

            # check if corresponding number exists in hashmap and if it is the same element being used
            if (
                target - nums[pointer] in count
                and count[target - nums[pointer]] != pointer
            ):
                return [count[target - nums[pointer]], pointer]

            pointer += 1
