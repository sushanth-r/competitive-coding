import collections


class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        node = self.children
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = "#"

    def search(self, word: str) -> bool:
        node = self.children
        for c in word:
            if c not in node:
                return False
            node = node[c]

        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.children
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


class ImplementTrie:
    x = Trie()
    x.insert("apple")
    x.insert("appl")
    print(x.search("apple"))
    print(x.search("app"))
    print(x.search("banana"))
    print(x.startsWith("app"))
    y = 3
