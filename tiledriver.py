'''
We the undersigned promise that we have in good faith attempted to
follow the principles of pair programming. Although we were free
to discuss ideas with others, the implementation is our own. We
have shared a common workspace and taken turns at the keyboard
for the majority of the work that we are submitting. Furthermore,
any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to
penalties as outlined in the course syllabus.

Signed Peter C Conant
Signed Bella Messina
9/29/2020

'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections

def driver() :
    n = 8
    puzzles = 31

    # Initialize data lists
    b_steps, b_nodes, b_time = [], [], []
    d_steps, d_nodes, d_time = [], [], []
    m_steps, m_nodes, m_time = [], [], []

    # Run puzzle trials on n size boards and add data to lists
    for i in range(0, puzzles):

        # BreadFirst call
        b_search = graph_search(NPuzzle(n=n, force_state=None, g=BreadthFirst.g, h=BreadthFirst.h))
        b_steps.append(len(b_search[0])) # Number of steps in BeardthFirst search
        b_nodes.append(b_search[1]) # Number of nodes explored in BeardthFirst search
        b_time.append(b_search[2]) # time spent in BeardthFirst search

        # DepthFirst call
        d_search = graph_search(NPuzzle(n=n, force_state=None, g=DepthFirst.g, h=DepthFirst.h))
        d_steps.append(len(d_search[0]))
        d_nodes.append(d_search[1])
        d_time.append(d_search[2])

        #Manhattan call
        m_search = graph_search(NPuzzle(n=n, force_state=None, g=Manhattan.g, h=Manhattan.h))
        m_steps.append(len(m_search[0]))
        m_nodes.append(m_search[1])
        m_time.append(m_search[2])

    # BreadthFirst
    b_steps_mean = mean(b_steps)
    b_steps_stdev = stdev(b_steps, b_steps_mean)
    b_nodes_mean = mean(b_nodes)
    b_nodes_stdev = stdev(b_nodes, b_nodes_mean)
    b_time_mean = mean(b_time)
    b_time_stdev = stdev(b_time, b_time_mean)

    len(b_search[0])
    print("Breadth First Search:")
    print("Mean steps: " + str(b_steps_mean))
    print("Standard Deviation steps: " + str(b_steps_stdev))
    print("Mean nodes: " + str(b_nodes_mean))
    print("Standard Deviation nodes: " + str(b_nodes_stdev))
    print("Mean time: " + str(b_time_mean))
    print("Standard Deviation time: " + str(b_time_stdev))
    print("----------------------------------")

    # DepthFirst
    d_steps_mean = mean(d_steps)
    d_steps_stdev = stdev(d_steps, d_steps_mean)
    d_nodes_mean = mean(d_nodes)
    d_nodes_stdev = stdev(d_nodes, d_nodes_mean)
    d_time_mean = mean(d_time)
    d_time_stdev = stdev(d_time, d_time_mean)

    print("Depth First Search:")
    print("Mean steps: " + str(d_steps_mean))
    print("Standard Deviation steps: " + str(d_steps_stdev))
    print("Mean nodes: " + str(d_nodes_mean))
    print("Standard Deviation nodes: " + str(d_nodes_stdev))
    print("Mean time: " + str(d_time_mean))
    print("Standard Deviation time: " + str(d_time_stdev))
    print("----------------------------------")


    # Manhattan
    m_steps_mean = mean(m_steps)
    m_steps_stdev = stdev(m_steps, m_steps_mean)
    m_nodes_mean = mean(m_nodes)
    m_nodes_stdev = stdev(m_nodes, m_nodes_mean)
    m_time_mean = mean(m_time)
    m_time_stdev = stdev(m_time, m_time_mean)

    print("A* Search:")
    print("Mean steps: " + str(m_steps_mean))
    print("Standard Deviation steps: " + str(m_steps_stdev))
    print("Mean nodes: " + str(m_nodes_mean))
    print("Standard Deviation nodes: " + str(m_nodes_stdev))
    print("Mean time: " + str(m_time_mean))
    print("Standard Deviation time: " + str(m_time_stdev))



if __name__ == '__main__':
    driver()
