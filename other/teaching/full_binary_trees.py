from copy import deepcopy
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []

        def helper(to_create: int):
            if to_create == 1: return [TreeNode()]

            created = []
            to_create -= 2
            for left in range(0, to_create + 1, 2):  #
                right = to_create - left

                left_copies = helper(left)
                right_copies = helper(right)

                for left_node in left_copies:
                    for right_node in right_copies:
                        new_node = TreeNode()
                        new_node.left = left_node
                        new_node.right = right_node
                        created.append(new_node)

            return created

        return helper(n)


def print_tree(roots: List[TreeNode]):
    for root in roots:
        values = []
        queue = [root]
        while queue:
            node = queue.pop()
            if node:
                values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append('null')
        print('[' + ','.join(map(str, values)) + ']')


print_tree(Solution().allPossibleFBT(3))
