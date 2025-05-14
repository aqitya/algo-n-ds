

###
### QUESTION
###

"""
RATING: 1933

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
"""




###
### Approach
###
"""
Thoughts: Overkill of a solution, don't have to use UF to solve the question, however, I wanted some UF practice (more so, 2D UF), so decided to go for it. Took a while to implement, 
          def not the approach you would want to take in an interview if time is a problem and/or you aren't very comfortable with UF implementations.

Intuition: I care about the overall size and the groupings of these components, so UF seemed like an obvious choice. After creating these groups, for each '0' in the grid,
           try to see if turning it into a '1' would combine any groupings, and if so, then add the total and add 1 (current position of the 0).

           The hardest part was debugging the actual function call where we are calculating the final ret value, as I was overcounting some values. This was combatted through tracking the 
           roots that were already processed at that current grid location. Furthermore, we may have been undercounting some values, only if we weren't returning the size of the root, instead, 
           returning the size of that current index in the UF.size struct. 
Runtime:
TC - O(N)
SC - O(N)

Note: there is a lot of overhead with this solution compared to the standard DFS approach. I believe the DFS approach would go something like, funding largest island,
      however, instead of stopping the traversal at a 0 and then backtracking, we keep track of a variable 'cond' and if true, we can explore once more in that direction.

      In other words, we are storing another dimension to the stack/queue (queue if you want to do BFS approach, which CAN work I believe?)
"""

from typing import List


class UnionFind:
  def __init__(self, size, grid):
    # UF = [[0 for _ in range(size)] for _ in range(size)]
    double_size = size * size
    UF = [0 for _ in range(double_size)]
    r = [0 for _ in range(double_size)]
    c = 0
    for i in range(size):
      for j in range(size):
        new_x = i * size
        UF[new_x + j] = c
        c += 1
        if grid[i][j] == 1:
          r[new_x + j] = 1
    self.sizes = r.copy()
    self.UF = UF
    self.r = r
    for x in range(size):
      for y in range(size):
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
          nx, ny = x + dx, y + dy
          if 0 <= nx < size and 0 <= ny < size and grid[x][y] == 1 and grid[nx][ny] == 1:
            u = x * size + y
            v = nx * size + ny
            self.merge(u, v)
    # print(self.UF)
    # print(self.r)
    # print(self.sizes)
  
  def find(self, root):
    if self.UF[root] == root:
      return root
    self.UF[root] = self.find(self.UF[root])
    return self.UF[root]

  def merge(self, u, v):
    root_u = self.find(u)
    root_v = self.find(v)
    if root_u == root_v:
      return
    r_u, r_v = self.rank(root_u), self.rank(root_v)
    # print(u, v, root_u, root_v)
    if r_u < r_v:
      self.UF[root_u] = root_v
      self.sizes[root_v] += self.sizes[root_u]
    elif r_v < r_u:
      self.UF[root_v] = root_u
      self.sizes[root_u] += self.sizes[root_v]
    else:
      self.UF[root_v] = root_u
      self.sizes[root_u] += self.sizes[root_v]
      self.r[root_u] += 1

  def rank(self, root):
    return self.r[root]

class Solution:
  def largestIsland(self, grid: List[List[int]]) -> int:
    size = len(grid)
    UF = UnionFind(size, grid)
    ret = min(max(UF.sizes) + 1, size * size)
    for x in range(size):
      for y in range(size):
        if grid[x][y] == 0:
          adj_sizes = 0
          seen_roots = set()
          for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 1:
              root = UF.find(nx * size + ny)
              if root not in seen_roots:
                adj_sizes += UF.sizes[root]
                seen_roots.add(root)
          ret = max(adj_sizes + 1, ret)
    return ret
