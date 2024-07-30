# https://leetcode.com/problems/search-suggestions-system
"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],[
    "mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.


Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
"""
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.suggestions = []


class TrieTree:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
            if len(current.suggestions) < 3:
                current.suggestions.append(word)

    def search(self, word: str) -> List[List[str]]:
        result = []
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                break
        result.extend([[]] * (len(word) - len(result)))
        return result

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = TrieTree()
        for pro in products:
            trie.insert(pro)
        return trie.search(searchWord)


products = ["havana"]
searchWord = "xxxxxx"
sol = Solution()
ans = sol.suggestedProducts(products, searchWord)
print(ans)
