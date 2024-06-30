class Trie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
    def insert(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        current.is_end_of_word = True
    
    def traverse(self):
        words = []
        self._traverse_recursive("", words)
        return words
    
    def _traverse_recursive(self, prefix, words):
        if self.is_end_of_word:
            words.append(prefix)
        for char, child_node in self.children.items():
            child_node._traverse_recursive(prefix + char, words)


trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("app")
trie.insert("apricot")

print(trie.traverse())
