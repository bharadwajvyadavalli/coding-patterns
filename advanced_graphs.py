"""
Advanced Graphs - NeetCode 75
Essential patterns for technical interviews.
"""

import heapq
from collections import defaultdict, deque

def find_itinerary(tickets):
    """LC 332 - Hierholzer's algorithm (Eulerian path)"""
    graph = defaultdict(list)
    for from_airport, to_airport in tickets:
        graph[from_airport].append(to_airport)
    
    for airport in graph:
        graph[airport].sort(reverse=True)
    
    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        result.append(airport)
    
    result = []
    dfs("JFK")
    return result[::-1]

def min_cost_connect_points(points):
    """LC 1584 - Kruskal's algorithm (MST)"""
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    n = len(points)
    parent = list(range(n))
    edges = []
    
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((manhattan_distance(points[i], points[j]), i, j))
    
    edges.sort()
    total_cost = 0
    edges_used = 0
    
    for cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return total_cost

def network_delay_time(times, n, k):
    """LC 743 - Dijkstra's algorithm"""
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0
    heap = [(0, k)]
    visited = set()
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    max_distance = max(distances.values())
    return max_distance if max_distance != float('inf') else -1

def critical_connections(n, connections):
    """LC 1192 - Tarjan's algorithm for bridges"""
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    discovery = [0] * n
    low = [0] * n
    time = [0]
    bridges = []
    
    def dfs(node, parent):
        discovery[node] = low[node] = time[0]
        time[0] += 1
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if discovery[neighbor] == 0:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], discovery[neighbor])
    
    for i in range(n):
        if discovery[i] == 0:
            dfs(i, -1)
    
    return bridges

def minimum_effort_path(heights):
    """LC 1631 - Binary search + BFS"""
    def can_reach_target(effort):
        m, n = len(heights), len(heights[0])
        visited = set()
        queue = [(0, 0)]
        visited.add((0, 0))
        
        while queue:
            i, j = queue.pop(0)
            if i == m - 1 and j == n - 1:
                return True
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n and 
                    (ni, nj) not in visited and
                    abs(heights[ni][nj] - heights[i][j]) <= effort):
                    visited.add((ni, nj))
                    queue.append((ni, nj))
        return False
    
    left, right = 0, 10**6
    while left < right:
        mid = left + (right - left) // 2
        if can_reach_target(mid):
            right = mid
        else:
            left = mid + 1
    return left

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

def dijkstra_shortest_path(graph, start):
    """Dijkstra's algorithm - shortest paths from start"""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

def bellman_ford(graph, start, n):
    """Bellman-Ford algorithm - handles negative weights"""
    distances = [float('inf')] * n
    distances[start] = 0
    
    for _ in range(n - 1):
        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    
    for u, v, w in graph:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return None  # Negative cycle
    
    return distances

def floyd_warshall(graph, n):
    """Floyd-Warshall - all pairs shortest path"""
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in graph:
        dist[u][v] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def kruskal_mst(edges, n):
    """Kruskal's algorithm - minimum spanning tree"""
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    parent = list(range(n))
    edges.sort(key=lambda x: x[2])
    
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break
    
    return mst, total_weight

def topological_sort(graph, n):
    """Topological sort - linear ordering of vertices"""
    visited = [False] * n
    result = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return result[::-1]

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print("Itinerary:", find_itinerary(tickets))
    
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print("Min Cost Connect Points:", min_cost_connect_points(points))
    
    times = [[2,1,1],[2,3,1],[3,4,1]]
    print("Network Delay Time:", network_delay_time(times, 4, 2))
    
    connections = [[0,1],[1,2],[2,0],[1,3]]
    print("Critical Connections:", critical_connections(4, connections))
    
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    print("Minimum Effort Path:", minimum_effort_path(heights)) 