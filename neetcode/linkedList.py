# https://neetcode.io/problems/singlyLinkedList

class LinkedList:
    
    def __init__(self):
        self.array = []

    def get(self, index: int) -> int:
        if index < len(self.array):
            return self.array[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        self.array.insert(0,val)
        
    def insertTail(self, val: int) -> None:
        self.array.append(val)

    def remove(self, index: int) -> bool:
        if index < len(self.array):
            self.array.pop(index)
            return True
        else: 
            return False

    def getValues(self) -> List[int]:
        return self.array
