# https://neetcode.io/problems/string-encode-and-decode


class Solution:
    """
    to decode effectively, we need to know where do the words break
    if we use a symbol, it's ineffective as it may pop up in the string and erroneously break the string into a word early
    hence we need to know the length of the string
    however, we cannot just use numbers as it may be a string of numbers, we won't know where it breaks
    we use a number and a symbol to mark the start of the string
    similar to computer networking concept

    to encode
    find length of string
    add symbol ;
    add string
    O(n) time, n is number of characters

    to decode
    find length n by taking numbers up to ;
    take the next n characters as a string
    repeat step 1 and 2
    O(n) time, n is number of characters
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += ";"
            res += string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        pointer, n = 0, len(s)
        res = []
        while pointer < n:
            length = ""
            while s[pointer] != ";":
                length += str(s[pointer])
                pointer += 1
            length = int(length)
            pointer += 1  # to skip over ";"
            string = ""
            for i in range(length):
                string += s[pointer]
                pointer += 1
            res.append(string)
        return res
