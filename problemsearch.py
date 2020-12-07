'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
from npuzzle import NPuzzle
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)

from explored import Explored
    
       
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored, elapsed_s) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    elapsed_s is the elapsed wall clock time performing the search
    """
    # Initializations
    time = Timer()
    initial = Node(problem=problem, state=problem.initial)
    queue = PriorityQueue()  # PriorityQueue based on lowest cost
    explored = Explored() # Set of explored nodes
    queue_expl = Explored() # Set of nodes inside the queue for

    # Set initial node into the queue
    queue.append(initial)
    queue_expl.add(initial.state)

    # Set variables
    done = found = False
    nodes_explored = 0

    while not done:
        node = queue.pop()                  # removed lowest cost state
        nodes_explored += 1                 # increment
        explored.add(node.state)            # add to explored set
        if problem.goal_test(node.state):   # if node is goal, exit with that node
            found = done = True
        else:
            children = node.expand(problem) # get child nodes of current node
            for child in children:
                if not explored.exists(child.state) and not queue_expl.exists(child.state):
                    queue.append(child)
                    queue_expl.add(child)
            if len(queue) == 0:
                done = True

    if(verbose):
        actions = node.solution()
        print("Solution in ", node.depth, "moves")
        for n in node.path():
           depth = n.depth
           if(depth == 0):
               print("Initial State")
           else:
               print("Move ",depth," - ",actions[depth-1])
           print(n.state)

    if not found:
        return None
    else:
        return (node.path(), nodes_explored, time.elapsed_s())
