from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue

def search(args):
    bt = BinaryTree()
    
    print("\nBuilding tree...")
    bt.create_from_file(args.file)
    print("Tree built")
    
    if args.order == "level-order":
        print("\nSearching tree...\n\n")
        target = args.word
        
        if bt.root.data == target:
            print("Word found!")
            return
        
        queue = Queue()
        queue.enqueue(bt.root)

        while queue.get_len():
            node = queue.dequeue()
            
            if node.left:
                if node.left.data == target:
                    print("Word Found!")            
                    return
                else:
                    queue.enqueue(node.left)

            if node.right:
                if node.right.data == target:
                    print("Word found!")
                    return
                else:
                    queue.enqueue(node.right)
            
        print("Word not found")
        return 
    
    print("breadth-first-search can only be used with --order 'level-order'")
    


# https://www.youtube.com/watch?v=224ZyGSxfMo&list=PL7g1jYj15RUMeIY778b8lvgUzdRFnEniI&index=3
