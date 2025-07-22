"""
Tries - NeetCode 75
Essential patterns for technical interviews.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    """LC 208 - Basic Trie operations"""
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class WordDictionary:
    """LC 211 - Trie with wildcard support"""
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end
        
        return dfs(0, self.root)

def find_words(board, words):
    """LC 212 - DFS with Trie for word search"""
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    def dfs(i, j, node, word):
        if node.is_end:
            result.add(word)
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        char = board[i][j]
        if char not in node.children:
            return
        
        board[i][j] = '#'
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj, node.children[char], word + char)
        board[i][j] = char
    
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, trie.root, "")
    
    return list(result)

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

class MapSum:
    """LC 677 - Trie with sum tracking"""
    def __init__(self):
        self.root = TrieNode()
        self.values = {}
    
    def insert(self, key, val):
        self.values[key] = val
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def sum(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        def dfs(node, current):
            total = 0
            if node.is_end:
                total += self.values.get(current, 0)
            for char, child in node.children.items():
                total += dfs(child, current + char)
            return total
        
        return dfs(node, prefix)

def replace_words(dictionary, sentence):
    """LC 648 - Replace with shortest root"""
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    
    def find_root(word):
        node = trie.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_end:
                return word[:i+1]
        return word
    
    words = sentence.split()
    return ' '.join(find_root(word) for word in words)

def suggested_products(products, searchWord):
    """LC 1268 - Trie with autocomplete"""
    trie = Trie()
    for product in products:
        trie.insert(product)
    
    def get_suggestions(prefix):
        node = trie.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        suggestions = []
        def dfs(node, current):
            if len(suggestions) >= 3:
                return
            if node.is_end:
                suggestions.append(current)
            for char in sorted(node.children.keys()):
                dfs(node.children[char], current + char)
        
        dfs(node, prefix)
        return suggestions
    
    result = []
    for i in range(len(searchWord)):
        result.append(get_suggestions(searchWord[:i+1]))
    
    return result

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests
    trie = Trie()
    trie.insert("apple")
    print("Search 'apple':", trie.search("apple"))
    print("StartsWith 'app':", trie.startsWith("app"))
    
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    print("Search 'b..':", word_dict.search("b.."))
    
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print("Word Search:", find_words(board, words)) 