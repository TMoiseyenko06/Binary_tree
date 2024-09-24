
class TreeNode():
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

class BinaryTree():
    def __init__(self):
        self.root_node = None

    def insert(self,key):
        if not self.root_node:
            self.root_node = TreeNode(key)
        else:
            self._insert_recursive(self.root_node,key)

    def _insert_recursive(self,node,key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left,key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right,key)

    def _delete_recursive(self,root,key):
        if root is None:
            return root
        
        if key < root.key:
            root.left = self._delete_recursive(root.left,key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._find_min_key(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)

    def _find_min_key(self,node):
        while node.left:
            node = node.left
        return node
    
    def tranversal_in_order(self):
        self._tranversal_in_order_recursive(self.root_node)

    def _tranversal_in_order_recursive(self,node):
        if node:
            self._tranversal_in_order_recursive(node.left)
            print(node.key, "  ")
            self._tranversal_in_order_recursive(node.right)

    def tranversal_pre_order(self):
        self._tranversal_pre_order_recursive(self.root_node)

    def _tranversal_pre_order_recursive(self,node):
        if node:
            print(node.key, "  ")
            self._tranversal_pre_order_recursive(node.left)
            self._tranversal_pre_order_recursive(node.right)

    def tranversal_post_order(self):
        self._tranversal_post_order_recursive(self.root_node)

    def _tranversal_post_order_recursive(self,node):
        if node:
            print(node.key, "  ")
            self._tranversal_post_order_recursive(node.left)
            self._tranversal_post_order_recursive(node.right)



keys = [1,2,5,7,9,6,3]
tree = BinaryTree()
for key in keys:
    tree.insert(key)

tree.tranversal_in_order()
tree.tranversal_pre_order()
tree.tranversal_post_order()