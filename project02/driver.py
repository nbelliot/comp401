from beam_search import *

if __name__ == "__main__":
    T = Tree()
    T.generate(5,3)
    T.printTree()
    
    BSearch = BeamSearch(T,6)