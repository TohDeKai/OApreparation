# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        """
        {()} - last one in has to be closed first
        LIFO -> stack
        whenever there is an open bracket, add it to the stack
        when there is a close bracket, pop from the stack
        if it is the corresponding open bracket, continue, else return false
        at the end, if the stack is empty, return true
        """
        stack = []
        pointer, n = 0, len(s)
        while pointer < n:
            if s[pointer] == "(" or s[pointer] == "[" or s[pointer] == "{":
                stack.append(s[pointer])
            else:
                if stack:
                    last = stack.pop()
                    if (
                        (last == "(" and s[pointer] != ")")
                        or (last == "[" and s[pointer] != "]")
                        or (last == "{" and s[pointer] != "}")
                    ):
                        return False
                    else:
                        pass
                else:
                    print("here2")
                    return False
            pointer += 1

        return len(stack) == 0
