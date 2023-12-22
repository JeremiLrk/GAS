class TreeItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

def createTreeItem(key, val):
    return TreeItem(key, val)

class BSTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, root, item):
        if root is None:
            return BSTNode(item)
        if item.key < root.item.key:
            root.left = self.insert(root.left, item)
        elif item.key > root.item.key:
            root.right = self.insert(root.right, item)
        return root

    def searchTreeInsert(self, item):
        if self.root is None:
            self.root = BSTNode(item)
            return True
        else:
            self.insert(self.root, item)
            return True

    def search(self, root, key):
        if root is None or root.item.key == key:
            return root
        if key < root.item.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def searchTreeRetrieve(self, key):
        node = self.search(self.root, key)
        if node is not None:
            return (node.item.value, True)
        return (None, False)

    def inorderTraverse(self, visit):
        def inorderTraverseHelper(root):
            if root is not None:
                inorderTraverseHelper(root.left)
                visit(root.item)
                inorderTraverseHelper(root.right)
        inorderTraverseHelper(self.root)

    def save(self):
        def serialize(node):
            if node is None:
                return None
            if node.left is None and node.right is None:
                return {'root': node.item.key}
            return {'root': node.item.key, 'children': [serialize(node.left), serialize(node.right)]}
        return serialize(self.root)

    def load(self, data):
        def deserialize(data):
            if data is None:
                return None
            node = BSTNode(createTreeItem(data['root'], data['root']))
            if 'children' in data and len(data['children']) == 2:
                node.left = deserialize(data['children'][0])
                node.right = deserialize(data['children'][1])
            return node
        self.root = deserialize(data)

    def delete(self, root, key):
        if root is None:
            return root, False
        if key < root.item.key:
            root.left, success = self.delete(root.left, key)
            return root, success
        elif key > root.item.key:
            root.right, success = self.delete(root.right, key)
            return root, success
        else:
            if root.left is None:
                return root.right, True
            elif root.right is None:
                return root.left, True
            temp = self.minValueNode(root.right)
            root.item = temp.item
            root.right, _ = self.delete(root.right, temp.item.key)
            return root, True

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def searchTreeDelete(self, key):
        self.root, success = self.delete(self.root, key)
        return success

def print_item(item):
    print(item.value)

if __name__ == "__main__":
    t = BST()
    print(t.isEmpty())
    print(t.searchTreeInsert(createTreeItem(8, 8)))
    print(t.searchTreeInsert(createTreeItem(5, 5)))
    print(t.isEmpty())
    print(t.searchTreeRetrieve(5)[0])
    print(t.searchTreeRetrieve(5)[1])
    t.inorderTraverse(print_item)
    print(t.save())
    t.load({'root': 10, 'children': [{'root': 5}, None]})
    t.searchTreeInsert(createTreeItem(15, 15))
    print(t.searchTreeDelete(0))
    print(t.save())
    print(t.searchTreeDelete(10))
    print(t.save())
