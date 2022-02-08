#재귀 함수 사용
from binary_search_tree import BinarySearchTree, NodeBST

class BSTwithTraversalRecursively(BinarySearchTree):
    
    def __init__(self):
        self.root= None
        self.nodes_BFS= []
        self.nodes_pre= []
        self.nodes_post= []
        self.nodes_in= []
        
    def BFS(self):
        self.root.level= 1
        queue= [self.root]
        current_level= self.root.level
        
        while len(queue)>0:
            current_node= queue.pop(0)
            if current_node.level>current_level:
                current_level+= 1
            self.nodes_BFS.append(current_node.value)
            
            if current_node.left:
                current_node.left.level= current_level+1
                queue.append(current_node.left)
                
            if current_node.right:
                current_node.right.level= current_level+1
                queue.append(current_node.right)
        
        return self.nodes_BFS
    
    def inorder(self, node=None, level=1):
        if not node and level==1:
            node= self.root
        if node:
            self.inorder(node.left, level+1)
            self.nodes_in.append(node.value)
            self.inorder(node.right, level+1)
        return self.nodes_in
    
    def preorder(self, node=None, level=1):
        if not node and level==1:
            node= self.root
        if node:
            self.nodes_pre.append(node.value)
            self.preorder(node.left, level+1)
            self.preorder(node.right, level+1)
        return self.nodes_pre
    
    def postorder(self, node=None, level=1):
        if not node and level==1:
            node= self.root
        if node:
            self.postorder(node.left, level+1)
            self.postorder(node.right, level+1)
            self.nodes_post.append(node.value)
        return self.nodes_post
    
if __name__== '__main__':
    bst= BSTwithTraversalRecursively()
    l= [10, 5, 6, 3, 8, 2, 1, 11, 9 ,4]
    for i in l:
        bst.add_node(i)
    
    print('노드 8은 말단 노드?', bst.is_leaf(8))
    print('노드 8의 레벨은?', bst.get_node_level(8))
    print('노드 10은 루트 노드?', bst.is_root(10))
    print('노드 1은 루트 노드?', bst.is_root(1))
    print('트리의 높이는?', bst.get_height())
    print('이진 탐색 트리?', bst.is_bst())
    print('균형 트리?', bst.is_balanced())
    
    print('전위 순회:', bst.preorder())
    print('후위 순회:', bst.postorder())
    print('중위 순회:', bst.inorder())
    print('너비 우선 순회:', bst.BFS())
    