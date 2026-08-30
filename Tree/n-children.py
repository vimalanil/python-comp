from collections import deque
from typing import List, Optional


# Definition for an N-ary tree node.
class Node:

  def __init__(
      self,
      val: Optional[int] = None,
      children: Optional[List["Node"]] = None,
  ):
    self.val = val
    self.children = children if children is not None else []


class NaryTreeTraversals:
  # 1. Preorder Traversal: Root -> Children (Left to Right)
  def preorder(self, root: Optional[Node]) -> List[int]:
    res = []

    def dfs(node):
      if not node:
        return
      res.append(node.val)  # Visit Root
      for child in node.children:  # Visit each child
        dfs(child)

    dfs(root)
    return res

  # 2. Postorder Traversal: Children (Left to Right) -> Root
  def postorder(self, root: Optional[Node]) -> List[int]:
    res = []

    def dfs(node):
      if not node:
        return
      for child in node.children:  # Visit all children first
        dfs(child)
      res.append(node.val)  # Visit Root

    dfs(root)
    return res

  # 3. Level-Order Traversal (BFS): Level by Level
  def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
    if not root:
      return []

    res = []
    queue = deque([root])

    while queue:
      level = []
      for _ in range(len(queue)):
        curr = queue.popleft()
        level.append(curr.val)
        for child in curr.children:
          queue.append(child)
      res.append(level)

    return res


def build_nary_tree(data: list) -> Optional[Node]:
  """Constructs an N-ary tree from LeetCode-style serialization where 'None'

  marks a level/sibling group break. Example: [1, None, 3, 2, 4, None, 5, 6]
  means:
     1 is root
     children of 1: [3, 2, 4]
     children of 3: [5, 6]
     children of 2: []
     children of 4: []
  """
  if not data or data[0] is None:
    return None

  root = Node(data[0])
  queue = deque([root])
  i = 2  # Skip root and the first None separator

  while queue and i < len(data):
    parent = queue.popleft()

    # Collect all siblings until the next None
    while i < len(data) and data[i] is not None:
      child = Node(data[i])
      parent.children.append(child)
      queue.append(child)
      i += 1

    i += 1  # Skip the None separator

  return root


# --- Example Test Run ---
if __name__ == "__main__":
  # Tree structure:
  #            1
  #        /   |   \
  #       3    2    4
  #      / \
  #     5   6
  tree_data = [1, None, 3, 2, 4, None, 5, 6]
  root = build_nary_tree(tree_data)

  traversals = NaryTreeTraversals()

  print(f"Serialized Input: {tree_data}\n")
  print(
      "Preorder   (Root -> Children):",
      traversals.preorder(root),
  )
  print(
      "Postorder  (Children -> Root):",
      traversals.postorder(root),
  )
  print(
      "Level Order (BFS by layers)  :",
      traversals.levelOrder(root),
  )