"""
Graph & Union-Find (Disjoint Set)

Graph is a data structure consisting of vertices and edges.
Union-Find is a data structure that tracks elements partitioned into disjoint subsets.
Common applications:
- Connected components
- Cycle detection in undirected graphs
- Minimum spanning tree (Kruskal's algorithm)
- Network connectivity
- Image segmentation

Time Complexity: O(α(n)) for union-find operations (α is inverse Ackermann)
Space Complexity: O(n) for storing parent and rank arrays
"""

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_count(self):
        return self.count

def number_of_provinces(is_connected):
    """
    Number of Provinces (LeetCode 547)
    Find number of connected components in undirected graph.
    """
    n = len(is_connected)
    uf = UnionFind(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    
    return uf.get_count()

def redundant_connection(edges):
    """
    Redundant Connection (LeetCode 684)
    Find edge that can be removed to form a tree.
    """
    n = len(edges)
    uf = UnionFind(n + 1)
    
    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return edge
    
    return []

def graph_valid_tree(n, edges):
    """
    Graph Valid Tree (LeetCode 261)
    Check if undirected graph forms a valid tree.
    """
    if len(edges) != n - 1:
        return False
    
    uf = UnionFind(n)
    
    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return False
    
    return uf.get_count() == 1

def accounts_merge(accounts):
    """
    Accounts Merge (LeetCode 721)
    Merge accounts with same email addresses.
    """
    uf = UnionFind(len(accounts))
    email_to_id = {}
    
    # Union accounts with same emails
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_id:
                uf.union(i, email_to_id[email])
            else:
                email_to_id[email] = i
    
    # Group emails by account
    id_to_emails = {}
    for email, id_val in email_to_id.items():
        root = uf.find(id_val)
        if root not in id_to_emails:
            id_to_emails[root] = set()
        id_to_emails[root].add(email)
    
    # Build result
    result = []
    for id_val, emails in id_to_emails.items():
        name = accounts[id_val][0]
        result.append([name] + sorted(emails))
    
    return result

def minimum_spanning_tree_kruskal(edges, n):
    """
    Minimum Spanning Tree using Kruskal's algorithm
    Find minimum cost to connect all vertices.
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    mst_edges = []
    total_cost = 0
    
    for edge in edges:
        u, v, weight = edge
        if uf.union(u, v):
            mst_edges.append(edge)
            total_cost += weight
            if uf.get_count() == 1:
                break
    
    return total_cost if uf.get_count() == 1 else -1

def number_of_islands_union_find(grid):
    """
    Number of Islands using Union-Find (LeetCode 200)
    Count islands in 2D grid using union-find.
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)
    
    # Count land cells
    land_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                land_count += 1
                current = r * cols + c
                
                # Check 4 directions
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < rows and 0 <= new_c < cols and 
                        grid[new_r][new_c] == '1'):
                        neighbor = new_r * cols + new_c
                        uf.union(current, neighbor)
    
    # Count connected components
    components = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                components.add(uf.find(r * cols + c))
    
    return len(components)

def friend_circles(is_connected):
    """
    Friend Circles (LeetCode 547) - Alternative approach
    Find number of friend circles in adjacency matrix.
    """
    n = len(is_connected)
    uf = UnionFind(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    
    return uf.get_count()

def regions_cut_by_slashes(grid):
    """
    Regions Cut By Slashes (LeetCode 959)
    Count regions formed by slashes in grid.
    """
    n = len(grid)
    uf = UnionFind(4 * n * n)
    
    for r in range(n):
        for c in range(n):
            base = 4 * (r * n + c)
            
            if grid[r][c] == '/':
                uf.union(base + 0, base + 3)
                uf.union(base + 1, base + 2)
            elif grid[r][c] == '\\':
                uf.union(base + 0, base + 1)
                uf.union(base + 2, base + 3)
            else:  # grid[r][c] == ' '
                uf.union(base + 0, base + 1)
                uf.union(base + 1, base + 2)
                uf.union(base + 2, base + 3)
            
            # Connect with neighbors
            if r > 0:  # Connect with top
                uf.union(base + 0, base - 4 * n + 2)
            if c > 0:  # Connect with left
                uf.union(base + 3, base - 4 + 1)
    
    return uf.get_count()

if __name__ == "__main__":
    # Test Number of Provinces
    print("=== Number of Provinces ===")
    is_connected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    result = number_of_provinces(is_connected)
    print(f"Number of provinces: {result}")
    
    # Test Redundant Connection
    print("\n=== Redundant Connection ===")
    edges = [[1, 2], [1, 3], [2, 3]]
    result = redundant_connection(edges)
    print(f"Redundant edge: {result}")
    
    # Test Graph Valid Tree
    print("\n=== Graph Valid Tree ===")
    n, edges = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]
    result = graph_valid_tree(n, edges)
    print(f"Is valid tree: {result}")
    
    # Test Accounts Merge
    print("\n=== Accounts Merge ===")
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    result = accounts_merge(accounts)
    print("Merged accounts:")
    for account in result:
        print(account)
    
    # Test Minimum Spanning Tree
    print("\n=== Minimum Spanning Tree ===")
    edges = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 2], [2, 3, 4]]
    n = 4
    result = minimum_spanning_tree_kruskal(edges, n)
    print(f"Minimum cost: {result}")
    
    # Test Number of Islands with Union-Find
    print("\n=== Number of Islands (Union-Find) ===")
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    result = number_of_islands_union_find(grid)
    print(f"Number of islands: {result}")
    
    # Test Friend Circles
    print("\n=== Friend Circles ===")
    is_connected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    result = friend_circles(is_connected)
    print(f"Number of friend circles: {result}") 