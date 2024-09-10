# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        return self.searchSkip(curr, word)

    def searchSkip(self, curr: TrieNode, word: str) -> bool:
        for i in range(len(word)):
            char = word[i]
            if char != ".":
                if char not in curr.children:
                    return False
                curr = curr.children[char]
            else:
                for child in curr.children.values():
                    if self.searchSkip(child, word[i + 1 :]):
                        return True
                return False
        return curr.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
