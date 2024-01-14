class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Create a hashmap to keep count of number of occurrence of each element
        iterate through the dictionary, sorting by its value
        return the top k elements

        O(mlogm) time complexity, m is number of unique numbers

        can optimise further:
        instead of sorting the dictionary
        create a bucket [] arr
        iterate through dict, let indice of bucket arr represent number of elements, also the value of the hashmap, key be the value of the arr.
        to find most frequent k elements, just select the k elements from the back
        we can do this because the answer is guaranteed to be unique
        """

        # creating hashmap
        count = {}

        # iterating through the list
        pointer, n = 0, len(nums)

        while pointer < n:
            if nums[pointer] not in count:
                count[nums[pointer]] = 1
            else:
                count[nums[pointer]] += 1
            pointer += 1

        # forming bucket
        bucket = [[] for i in range(n + 1)]

        for key, value in count.items():
            bucket[value].append(key)

        count_k, res = 0, []

        for i in bucket[::-1]:
            if i != []:
                for j in i:
                    res.append(j)
                    count_k += 1
                    if count_k == k:
                        return res
