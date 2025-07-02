from typing import List


class TrieNode:
    def __init__(self):
        self.digits = [None] * 10
        self.end = False

    def contains(self, key: chr) -> bool:
        return self.digits[int(key)] is not None

    def put(self, key: chr, node: "TrieNode") -> None:
        self.digits[int(key)] = node

    def get(self, key: chr) -> "TrieNode":
        return self.digits[int(key)]

    def is_end(self) -> bool:
        return self.end

    def set_end(self) -> None:
        self.end = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number: int) -> None:
        number = str(number)
        curr = self.root

        for char in number:
            if not curr.contains(char):
                curr.put(char, TrieNode())
            curr = curr.get(char)

        curr.set_end()

    def prefix_length(self, number: int) -> int:
        i = 0
        number = str(number)
        curr = self.root

        for char in number:
            if not curr.contains(char):
                break
            i += 1
            curr = curr.get(char)

        return i


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        trie = Trie()
        for x in arr1:
            trie.insert(x)

        longest = 0
        for y in arr2:
            longestPrefix = trie.prefix_length(y)
            longest = max(longest, longestPrefix)

        return longest
