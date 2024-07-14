# https://leetcode.com/problems/time-based-key-value-store/description/


class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = [(value, timestamp)]
        else:
            self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pointer = 0
        res = ""
        if key not in self.hm:
            return res
        l, r = 0, len(self.hm[key]) - 1
        while l <= r:
            pointer = (l + r) // 2
            if self.hm[key][pointer][1] <= timestamp:
                res = self.hm[key][pointer][0]
                l = pointer + 1
            else:
                r = pointer - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
