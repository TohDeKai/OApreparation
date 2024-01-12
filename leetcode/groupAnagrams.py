# https://leetcode.com/problems/group-anagrams/description/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Create a hashmap, where the sorted str will act as the key and a list of the annegrams with the same sorted str will be the value.
        Iterate through the strs, sort each str and check if inside hashmap.
        If it is, append the str to the list. If not, add to the hashmap as a list.
        After iterating through the list of strs, iterate through the hashmap.
        For each key-value pair, add the value (which is a list) to the results list.
        return results list

        sorting will be O(nlogn)
        so time complexity will be O(mnlog(n)), where n is the length of the string and m is the number of strings
        """

        # creating hashmap
        anagrams = {}

        # iterating through the list
        pointer, n = 0, len(strs)
        while pointer < n:
            sortedStr = "".join(sorted(strs[pointer]))
            if sortedStr in anagrams:
                anagrams[sortedStr].append(strs[pointer])
            else:
                anagrams[sortedStr] = [strs[pointer]]
            pointer += 1

        # creating result list
        res = []

        for anagram in anagrams:
            res.append(anagrams[anagram])

        return res
