'''
Approach: WordTree, DepthFirstSearch
Time Complexity: O(mn)
Space Complexity: O(mn)
'''

class TreeNode():
    def __init__(self):
        self.children = {}
        self.isFull = False

class Boggle:
    def __init__(self, word_lst):
        self.start = TreeNode()
        self.grid = None
        self.result = set()

        # Inserting words from wordList into the WordTree
        for word in word_lst:
            self.insert(word)

    def insert(self, word):
        node = self.start
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.isFull = True

    def searchWords(self, board):
        self.grid = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.depthFirstSearch(i, j, self.start, "")
        return list(self.result)

    def depthFirstSearch(self, i, j, treeNode, currentWord):
        if treeNode.isFull:
            self.result.add(currentWord)

        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]):
            return

        ls = self.grid[i][j]
        if ls not in treeNode.children:
            return

        self.grid[i][j] = "#"

        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            self.depthFirstSearch(i+dx, j+dy, treeNode.descendants[ls], currentWord+ls)

        self.grid[i][j] = ls

# Sample Usage:

game = Boggle([ "ace", "ape", "cape", "clap", "clay", "gape", "grape", "lace", "lap", "lay", "mace", "map", "may", "pace",
"pay", "rap", "ray", "tap", "tape", "trace", "trap", "tray", "yap"
])

output = game.searchWords([['a', 'd', 'e'],['r', 'c', 'p'],['l', 'a', 'y']])
print(output)
