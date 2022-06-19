import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.suggestions = []

    def insert(self, product):
        temp = self
        for c in product:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
            temp.suggestions.append(product)
            temp.suggestions.sort()
            if len(temp.suggestions) > 3:
                temp.suggestions.pop()


class Solution:
    def suggestedProducts(self, products: List[str], search_word: str) -> List[List[str]]:
        trie_node = TrieNode()
        for product in products:
            trie_node.insert(product)

        result = list()
        temp = trie_node
        start = len(search_word)
        for i in range(len(search_word)):
            c = search_word[i]
            if c not in temp.children:
                start = i
                break
            suggestions = temp.children[c].suggestions
            if len(suggestions) > 3:
                result.append(suggestions[0: 3])
            else:
                result.append(suggestions)
            temp = temp.children[c]

        for _ in range(start, len(search_word)):
            result.append([])
        return result


class SearchSuggestionSystem:
    # products = list(map(str, input().split()))
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = str(input())
    x = Solution().suggestedProducts(products, search_word)
    print(x)
