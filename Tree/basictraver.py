from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

  def __init__(
      self,
      val: int = 0,
      left: Optional["TreeNode"] = None,
      right: Optional["TreeNode"] = None,
  ):
    self.val = val
    self.left = left
    self.right = right


class TreeTraversals:
  # 1. Inorder Traversal: Left -> Root -> Right
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def trav(node):
      if not node:
        return
      trav(node.left)  # Left
      res.append(node.val)  # Root
      trav(node.right)  # Right

    trav(root)
    return res

  # 2. Preorder Traversal: Root -> Left -> Right
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def trav(node):
      if not node:
        return
      res.append(node.val)  # Root
      trav(node.left)  # Left
      trav(node.right)  # Right

    trav(root)
    return res

  # 3. Postorder Traversal: Left -> Right -> Root
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def trav(node):
      if not node:
        return
      trav(node.left)  # Left
      trav(node.right)  # Right
      res.append(node.val)  # Root

    trav(root)
    return res


def build_tree_from_list(values: list) -> Optional[TreeNode]:
  """Constructs a binary tree from a level-order list."""
  if not values or values[0] is None:
    return None

  root = TreeNode(values[0])
  queue = deque([root])
  i = 1

  while queue and i < len(values):
    curr = queue.popleft()

    # Left child
    if i < len(values) and values[i] is not None:
      curr.left = TreeNode(values[i])
      queue.append(curr.left)
    i += 1

    # Right child
    if i < len(values) and values[i] is not None:
      curr.right = TreeNode(values[i])
      queue.append(curr.right)
    i += 1

  return root


# --- Example Test Run ---
if __name__ == "__main__":
  # Tree structure:
  #        1
  #       / \
  #      2   3
  #     / \
  #    4   5
  tree_values = [1, 2, 3, 4, 5]
  root = build_tree_from_list(tree_values)

  traversals = TreeTraversals()

  print(f"Tree (Level-order): {tree_values}\n")
  print(
      f"Preorder  (Root -> Left -> Right): {traversals.preorderTraversal(root)}"
  )
  print(
      f"Inorder   (Left -> Root -> Right): {traversals.inorderTraversal(root)}"
  )
  print(
      f"Postorder (Left -> Right -> Root): {traversals.postorderTraversal(root)}"
  )