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

trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("app")
trie.insert("apricot")