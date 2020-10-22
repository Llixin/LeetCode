class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def myprint(self) -> None:
        def pprint(root):
            for c in root.children:
                print(c, ':{', end=' ')
                pprint(root.children[c])
            print('}', end=' ')
        pprint(self.root)
        print()

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isWord = True
        # self.myprint()

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.isWord

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True


trie = Trie()
words = ["app", "apple", "book", "bother", "cat"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))
print(trie.search("break"))
print(trie.startsWith("ap"))
print(trie.startsWith("bu"))
