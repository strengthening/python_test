#-*- encoding=utf-8 -*-  

## 14 二叉树节点
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BTree():

    def __init__(self,):
        self.root = None

    def create_lookup_Tree(self,arr, n , sub):
        if sub >= n:
            return None
        newnode = Node(arr[sub])

        if self.root == None:
            self.root = newnode

        newnode.left = self.create_lookup_Tree(arr, n , 2 * sub + 1)
        newnode.right = self.create_lookup_Tree(arr, n , 2 * sub + 2)
        return newnode

    def pre_Order(self, root):
        if root is not None:
            print root.data
            self.pre_Order(root.left)
            self.pre_Order(root.right)


    def in_Order(self, root):
        if root is not None:            
            self.in_Order(root.left)
            print root.data
            self.in_Order(root.right)

    def post_Order(self, root):
        if root is not None:
            self.post_Order(root.left)
            self.post_Order(root.right)
            print root.data
    '''
    广度优先搜索算法 (BFS) Breadth First Search    
    ----------------------------------------
    借助队列数据结构，由于队列是先进先出的顺序，因此可以先将左子树入队，然后再将右子树入队。
    这样一来，左子树结点就存在队头，可以先被访问到。
    '''
    def lookup(self, root):
        queue = [root]
        while queue:
            current = queue.pop(0)
            print current.data
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    '''
    深度优先搜索算法 (DFS) （Depth First Search）
    -----------------------------------------
    分析一下，在遍历了根结点后，就开始遍历左子树，最后才是右子树。
    因此可以借助堆栈的数据结构，由于堆栈是后进先出的顺序，由此可以先将右子树压栈，然后再对左子树压栈，
    这样一来，左子树结点就存在了栈顶上，因此某结点的左子树能在它的右子树遍历之前被遍历。
    '''
    def deep(self,root):
        stack = [root]
        while stack:
            current = stack.pop(len(stack)-1)
            print current.data
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def maxDepth(self,root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def invert(self,root):
        if root.left != None and root.right != None:
            root.left , root.right = root.right , root.left
            self.invert(root.left)
            self.invert(root.right)


if __name__ == '__main__':

    arr = [100, 4, 2, 3, 15, 35, 6, 45, 55, 20, 1, 14, 56, 57, 58]
    tree = BTree()
    tree.create_lookup_Tree(arr , len(arr) , 0)

    print "前序遍历"
    tree.pre_Order(tree.root)

    print "中序遍历"
    tree.in_Order(tree.root)

    print "后序遍历"
    tree.post_Order(tree.root)

    print "层次遍历"
    tree.lookup(tree.root)

    print "深度遍历"
    tree.deep(tree.root)

    print "求最大树深"
    print tree.maxDepth(tree.root)

    tree.lookup(tree.root)
    print "二叉树反转"
    tree.invert(tree.root)
    tree.lookup(tree.root)