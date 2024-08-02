# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.array = []
        self.minarray = []
        self.length = 0

    def push(self, val: int) -> None:
        if len(self.array) == 0:
            self.minarray.append(val)
        else:
            if val < self.minarray[self.length - 1]:
                self.minarray.append(val)
            else:
                self.minarray.append(self.minarray[self.length - 1])
        self.array.append(val)
        self.length += 1

    def pop(self) -> None:
        self.array.pop(-1)
        self.minarray.pop(-1)
        self.length -= 1

    def top(self) -> int:
        return self.array[self.length - 1]

    def getMin(self) -> int:
        return self.minarray[self.length - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
