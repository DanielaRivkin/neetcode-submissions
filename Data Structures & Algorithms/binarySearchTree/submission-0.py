class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def _insert(node, key, val):
            if node is None:
                return TreeNode(key, val)
            if key < node.key:
                node.left = _insert(node.left, key, val)
            elif key > node.key:
                node.right = _insert(node.right, key, val)
            else:
                node.value = val  # Override existing value
            return node

        self.root = _insert(self.root, key, val)

    def get(self, key: int) -> int:
        def _get(node, key):
            if node is None:
                return -1
            if key < node.key:
                return _get(node.left, key)
            elif key > node.key:
                return _get(node.right, key)
            else:
                return node.value

        return _get(self.root, key)

    def getMin(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def getMax(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def remove(self, key: int) -> None:
        def _remove(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # Find in-order successor
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.key, node.value = successor.key, successor.value
                node.right = _remove(node.right, successor.key)
            return node

        self.root = _remove(self.root, key)

    def getInorderKeys(self):
        result = []

        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)

        _inorder(self.root)
        return result
