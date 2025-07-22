"""
Graphs - DFS & BFS - NeetCode 75
Essential patterns for technical interviews.
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def num_islands(grid):
    """LC 200 - DFS to mark connected land cells"""
    if not grid:
        return 0
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

def clone_graph(node):
    """LC 133 - DFS with hash map"""
    if not node:
        return None
    
    def dfs(original, visited):
        if original in visited:
            return visited[original]
        
        cloned = Node(original.val)
        visited[original] = cloned
        
        for neighbor in original.neighbors:
            cloned.neighbors.append(dfs(neighbor, visited))
        
        return cloned
    
    return dfs(node, {})

def pacific_atlantic(heights):
    """LC 417 - DFS from both oceans, find intersection"""
    if not heights:
        return []
    
    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    
    def dfs(i, j, ocean, prev_height):
        if (i < 0 or i >= m or j < 0 or j >= n or 
            (i, j) in ocean or heights[i][j] < prev_height):
            return
        
        ocean.add((i, j))
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj, ocean, heights[i][j])
    
    for i in range(m):
        dfs(i, 0, pacific, float('-inf'))
        dfs(i, n-1, atlantic, float('-inf'))
    for j in range(n):
        dfs(0, j, pacific, float('-inf'))
        dfs(m-1, j, atlantic, float('-inf'))
    
    return list(pacific & atlantic)

def can_finish(num_courses, prerequisites):
    """LC 207 - Topological sort with cycle detection"""
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = [i for i in range(num_courses) if in_degree[i] == 0]
    count = 0
    
    while queue:
        course = queue.pop(0)
        count += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == num_courses

def find_order(num_courses, prerequisites):
    """LC 210 - Topological sort with path reconstruction"""
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = [i for i in range(num_courses) if in_degree[i] == 0]
    result = []
    
    while queue:
        course = queue.pop(0)
        result.append(course)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == num_courses else []

def oranges_rotting(grid):
    """LC 994 - Multi-source BFS"""
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    queue = []
    fresh = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    minutes = 0
    while queue and fresh > 0:
        minutes += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            i, j = queue.pop(0)
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1):
                    grid[ni][nj] = 2
                    queue.append((ni, nj))
                    fresh -= 1
    
    return minutes if fresh == 0 else -1

def walls_and_gates(rooms):
    """LC 286 - Multi-source BFS from gates"""
    if not rooms:
        return
    
    m, n = len(rooms), len(rooms[0])
    queue = []
    
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
    
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == float('inf')):
                rooms[ni][nj] = rooms[i][j] + 1
                queue.append((ni, nj))

def find_cheapest_price(n, flights, src, dst, k):
    """LC 787 - BFS with price tracking"""
    graph = [[] for _ in range(n)]
    for u, v, w in flights:
        graph[u].append((v, w))
    
    queue = [(src, 0)]
    prices = [float('inf')] * n
    prices[src] = 0
    
    for _ in range(k + 1):
        level_size = len(queue)
        for _ in range(level_size):
            city, total_price = queue.pop(0)
            for neighbor, price in graph[city]:
                new_price = total_price + price
                if new_price < prices[neighbor]:
                    prices[neighbor] = new_price
                    queue.append((neighbor, new_price))
    
    return prices[dst] if prices[dst] != float('inf') else -1

def valid_tree(n, edges):
    """LC 261 - Union-Find with cycle detection"""
    if len(edges) != n - 1:
        return False
    
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True
    
    for x, y in edges:
        if not union(x, y):
            return False
    
    return True

def count_components(n, edges):
    """LC 323 - Union-Find"""
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    for x, y in edges:
        union(x, y)
    
    return len(set(find(i) for i in range(n)))

def alien_order(words):
    """LC 269 - Topological sort with graph construction"""
    if not words:
        return ""
    
    graph = {char: set() for word in words for char in word}
    in_degree = {char: 0 for char in graph}
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
        else:
            if len(word1) > len(word2):
                return ""
    
    queue = [char for char in in_degree if in_degree[char] == 0]
    result = []
    
    while queue:
        char = queue.pop(0)
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return ''.join(result) if len(result) == len(graph) else ""

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

def all_paths_source_target(graph):
    """LC 797 - DFS with backtracking"""
    def dfs(node, path):
        if node == len(graph) - 1:
            result.append(path[:])
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()
    
    result = []
    dfs(0, [0])
    return result

def is_bipartite(graph):
    """LC 785 - BFS with coloring"""
    n = len(graph)
    colors = [-1] * n
    
    for i in range(n):
        if colors[i] == -1:
            queue = [i]
            colors[i] = 0
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
    return True

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests
    grid = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
    print("Number of Islands:", num_islands(grid))
    
    print("Can Finish Courses:", can_finish(4, [[1,0],[2,0],[3,1],[3,2]]))
    print("Course Order:", find_order(4, [[1,0],[2,0],[3,1],[3,2]]))
    
    rooms = [[float('inf'),-1,0,float('inf')], [float('inf'),float('inf'),float('inf'),-1], [float('inf'),-1,float('inf'),-1], [0,-1,float('inf'),float('inf')]]
    walls_and_gates(rooms)
    print("Walls and Gates:", rooms) 