"""
copy and paste UF class for coding contest.

to use, assign UF = UnionFind(n), where n is size of UF DS.

has path compression for find and uses rank size for union for efficient unions.
"""

class UnionFind:
  def __init__(self, size):
    self.rank = [0] * size
    self.parent = list(range(size))
    self.size = [0] * size
  
  def find(self, curr):
    if self.parent[curr] == curr:
      return curr
    self.parent[curr] = self.find(self.parent[curr])
    return self.parent[curr]

  def union(self, u, v):
    u_root = self.find(u)
    v_root = self.find(v)
    if u_root != v_root:
      if self.rank[u_root] < self.rank[v_root]:
        self.parent[u_root] = v_root
        self.size[v_root] += self.size[u_root]
      elif self.rank[u_root] > self.rank[v_root]:
        self.parent[v_root] = u_root
        self.size[u_root] += self.size[v_root]
      else:
        self.root[u_root] += 1
        self.root[v_root] = u_root
        self.size[u_root] += self.size[v_root]
  
  def size(self, curr):
    return self.size[curr]

