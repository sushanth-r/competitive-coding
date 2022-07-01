class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(k, node):
            for i in range(k, len(word)):
                if word[i] == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    else:
                        node = node.children[word[i]]
            return node.end_of_word

        return dfs(0, self.root)


class DesignAddAndSearchWordDataStructure:
    x = WordDictionary()
    x.addWord("bad")
    x.addWord("dad")
    x.addWord("mad")
    print(x.search("pad"))
    print(x.search("bad"))
    print(x.search(".ad"))
    print(x.search("bs."))
