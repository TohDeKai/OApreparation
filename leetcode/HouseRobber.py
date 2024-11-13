# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        starting from the back
        from for every house
        you check 2 across,skipping the one beside, and then you add because that's the possible houses you can rob

        100 0 0 100
        100 100 0 100
        """

        n = len(nums)
        if n == 3:
            return max(nums[1],nums[0] + nums[2])
        elif n < 3:
            return max(nums)
        else:
            pointer = n - 3
            nums[pointer] += nums[pointer+2]
            pointer -= 1

            while pointer >= 0:
                nums[pointer] += max(nums[pointer+2],nums[pointer+3])
                pointer -= 1
                print(nums)
    
        return max(nums[0],nums[1])