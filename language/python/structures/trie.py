class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        words = []
        self._collect_words(current, prefix, words)
        return words

    def _collect_words(self, node, prefix, words):
        if node.end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix+char, words)

trie = Trie()
words = ["cat", "car", "cart", "carbon", "dog", "door"]
for word in words:
    trie.insert(word)

print(trie.search("car"))      # True
print(trie.search("care"))     # False

print(trie.starts_with("car"))  # ['car', 'cart', 'carbon']
print(trie.starts_with("do"))   # ['dog', 'door']
print(trie.starts_with("ca"))   # ['cat', 'car', 'cart', 'carbon']
print(trie.starts_with("z"))    # []