class Solution:
    # https://leetcode.com/problems/generate-parentheses/

    def generateParenthesis(self, n: int) -> List[str]:
        """
        concept here is that using recursion, we can form every possible combi using the stack
        as long as the number of open brackets is less than n, it is still possible, we can append an open bracket to it.
        after appending and continuing backtracking, we need to pop it since the stack is being used after

        as long as number of close brackets is less than open brackets, still possbile to add close bracket, so we add backtracking to it

        when close bracket == open bracket == n, it is a completed combi of a well-formed parentheses, append it to results
        """
        stack = []
        res = []

        def backTrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backTrack(openN, closeN + 1)
                stack.pop()

        backTrack(0, 0)
        return res
