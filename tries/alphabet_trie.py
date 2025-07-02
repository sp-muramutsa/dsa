class TrieNode:
    def __init__(self):
        self.alphabets = [None] * 26
        self.end = False

    def contains_key(self, key: str) -> bool:
        return self.alphabets[ord(key) - ord("a")] is not None

    def get(self, key: str) -> "TrieNode":
        return self.alphabets[ord(key) - ord("a")]

    def put(self, key: str, node: "TrieNode"):
        self.alphabets[ord(key) - ord("a")] = node

    def set_end(self) -> None:
        self.end = True

    def check_end(self) -> bool:
        return self.end


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if not curr.contains_key(char):
                curr.put(char, TrieNode())
            curr = curr.get(char)
        curr.set_end()

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if not curr.contains_key(char):
                return False
            curr = curr.get(char)

        # Word is contained but only as a prefix.
        if not curr.check_end():
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if not curr.contains_key(char):
                return False
            curr = curr.get(char)

        return True


trie = Trie()
trie.insert("kingsley")
param_1 = trie.search("kingsley")
print(param_1)
trie.insert("king")
param_2 = trie.startsWith("king")
print(param_2)
