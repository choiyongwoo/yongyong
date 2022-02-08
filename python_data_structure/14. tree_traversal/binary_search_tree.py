from binary_tree import NodeBT, BinaryTree

class NodeBST(NodeBT):
    
    def __init__(self, value=None, level=1):
        self.value= value
        self.level= level
        self.left= None
        self.right= None
        
    def _add_next_node(self, value, level_here=2):
        new_node= NodeBST(value, level_here)
        if value>self.value:
            self.right= self.right and self.right._add_next_node(value, level_here+1) or new_node
        elif value<self.value:
            self.left= self.left and self.left._add_next_node(value, level_here+1) or new_node
        else:
            print('중복 노드를 허용하지 않음')
        return self
    
    def _search_for_node(self, value):
        if self.value== value:
            return self
        elif self.left and value<self.value:
            return self.left._search_for_node(value)
        elif self.right and value>self.value:
            return self.right._search_for_node(value)
        else:
            return False
        
class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root= None
        
    def add_node(self, value):
        if not self.root:
            self.root= NodeBST(value)
        else:
            self.root._add_next_node(value)
            
if __name__== '__main__':
    bst= BinarySearchTree()
    for i in [6, 4, 8, 2, 5, 7, 9, 1, 3]:
        bst.add_node(i)
    print('노드 8은 말단 노드입니까?', bst.is_leaf(8))
    print('노드 8의 레벨은?', bst.get_node_level(8))
    print('노드 10은 루트 노드입니까?', bst.is_root(10))
    print('노드 1은 루트 노드입니끼?', bst.is_root(1))
    print('트리의 높이는?', bst.get_height())
    print('이진 탐색 트리입니까?', bst.is_bst())
    print('균형 트리입니까?', bst.is_balanced())