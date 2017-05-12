#-*- encoding=utf-8 -*-  

## 14 二叉树节点
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree():
    def __init__(self,):
        self.root = None

    def create_lookup_Tree(arr, n , sub):
        if sub >= n:
            return None

        newnode = Node(arr[sub])
        if self.root == None:
            



def pre_Order(root):
    if root is not None:
        print root.data
        pre_Order(root.left)
        pre_Order(root.right)

def in_Order(root):
    if root is not None:
        
        in_Order(root.left)
        print root.data
        in_Order(root.right)

def post_Order(root):
    if root is not None:        
        post_Order(root.left)        
        post_Order(root.right)
        print root.data

def lookup(root):
    stack = [root]
    print stack
    while stack:
        current = stack.pop(0)
        print current.data
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
        # print '~~~~~~~~~~~~'

# def deep(root):


if __name__ == '__main__':
    # tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

    # pre_Order(tree)
    # print '~~~~'
    # in_Order(tree)
    # print '~~~~'
    # post_Order(tree)

    # lookup(tree)
    tree = Tree()