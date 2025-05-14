

"""
SIMPLE SEGMENT TREE IMPLEMENTATION

useful for 'range queries' questions in O(log(n)) time. With n queries, the runtime is O(n*log(n)).

This specific implementation is for solving the Range Sum Query Problem, where we are interested in the summation of a range of values from the left to right indexs.

Furthermore, we support update operations to the entire tree.

"""


class SegmentTree:
  def __init__(self, a):
    n = len(a)
    self.t = [0] * (4 * n) # this will be the actual tree
    n -= 1

    
    def build(idx, l, r):
      if l == r:
        self.t[idx] = a[r]
      else:
        mid = (l + r) // 2
        build(idx * 2, l, mid)
        build(idx * 2 + 1, mid + 1, r)
        self.t[idx] = self.t[idx * 2]  + self.t[idx * 2 + 1]
    
    build(1, 0, n) # builds the segment tree


    self.n = n
    # debug print statement
    # print(self.t)

  def update(self, i, val):
    def _update(idx, nodeL, nodeR):
      if nodeL == nodeR:
        self.t[idx] = val        
      else:
        mid = (nodeL + nodeR) // 2
        if i <= mid:
          _update(idx * 2, nodeL, mid)
        else:
          _update(idx * 2 + 1, mid + 1, nodeR)
        self.t[idx] = self.t[idx * 2] + self.t[idx * 2 + 1]
    _update(1, 0, self.n)
    return None

  def query(self, l, r):
    def _query(idx, nodeL, nodeR):
      # no overlap
      if r < nodeL:
        return 0
      if l > nodeR:
        return 0
      
      # total overlap.
      if l <= nodeL and nodeR <= r:
        return self.t[idx]
      
      # partial overlap
      nodeMid = (nodeL + nodeR) // 2
      left = _query(idx * 2, nodeL, nodeMid)
      right = _query(idx * 2 + 1, nodeMid + 1, nodeR)
      return left + right
    return _query(1, 0, self.n)
  

  # str repr of ST.
  def __repr__(self):
    return str(self.t)

ST = SegmentTree([1, 3, 5])
print(ST.query(1,2))
print(ST.update(1, 2))
print(ST)
print(ST.query(1,2))
