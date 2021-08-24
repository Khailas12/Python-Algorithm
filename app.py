import argparse
from search import breadth_first
from search import depth_first
from search import binary


def main():
    # arg parser 
    parser = argparse.ArgumentParser(description="Search for word in file")
    
    # word
    parser.add_argument(
        "-w",
        "--word",
        required=True,
        help="Word to be Searched for"
    )
    
    # file
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to the file is to be Searched for"
    )
    
    # algorithm
    parser.add_argument(
        "-sa",
        "--search-algorithm",
        choices=["binary-search", "depth-first-search", "breadth-first-search"],
        required=True,
        help="Algorith to be used to Search for file"
    )
    
    # order
    parser.add_argument(
        "-o",
        "--order",
        choices=["pre-order", "post-order", "in-order", "level-order"],
        required=True,
        help="The order which treverse the tree"
    )
    
    # storing all arguments in this args variable
    args = parser.parse_args()      # In terminal -> n app.py -w "word" -f app.py -o pre-order -sa depth-first-search
    # print(f"\n\n{args}")
    # print(f"\n{args.search_algorithm}")
    
    # depth first search
    if args.search_algorithm == "depth-first-search":
        depth_first.search(args)
        return
    
    # breadth first search
    if args.search_algorithm == "breadth-first-search":
        breadth_first.search(args)
        return
    
    # binary search
    if args.search_algorithm == "binary-search":
        binary.search(args)
        return
    

if __name__ == "__main__":
    main()
    
print("\n\nDone")

