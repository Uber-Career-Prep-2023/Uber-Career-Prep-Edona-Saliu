# Space: O(m*n) (m: words, n: avg word length)
# Time: O(word length) (insert, isValidWord),
#       O(longest word length) (remove)

#Time spent: 40 mins


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for n in word:
            if n not in current_node.children:
                current_node.children[n] = TrieNode()
            current_node = current_node.children[n]
        current_node.end = True

    def isValidWord(self, word):
        current_node = self.root
        for n in word:
            if n not in current_node.children:
                return False
            current_node = current_node.children[n]
        return current_node.end == True

    def remove(self,word):
        def _remove(node, word, indx):
            if indx == len(word):
                node.end = False
                return len(node.children) == 0

            letter = word[indx]
            if letter not in node.children:
                return False

            child_node = node.children[letter]
            remove_child = _remove(child_node, word, indx + 1)

            if remove_child:
                del node.children[letter]
                return len(node.children) == 0 and not node.end

            return False

        _remove(self.root, word, 0)

# Create a Trie instance
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")
trie.insert("batman")

# Test isValidWord method
print(trie.isValidWord("apple"))    # True
print(trie.isValidWord("app"))      # True
print(trie.isValidWord("banana"))   # True
print(trie.isValidWord("bat"))      # True
print(trie.isValidWord("batman"))   # True
print(trie.isValidWord("apples"))   # False
print(trie.isValidWord("ban"))      # False

# Test remove method
trie.remove("apple")
trie.remove("bat")
trie.remove("app")

print(trie.isValidWord("apple"))    # False
print(trie.isValidWord("app"))      # False
print(trie.isValidWord("banana"))   # True
print(trie.isValidWord("bat"))      # False
print(trie.isValidWord("batman"))   # True
