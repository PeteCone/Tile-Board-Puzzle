

from basicsearch_lib02.tileboard import TileBoard
from npuzzle import NPuzzle


def human_player():
    size = 8  # N puzzle

    # Create a problem representation
    problem = NPuzzle(size)

    state = problem.initial # Get the initial state

    # Did we get lucky?
    solved = problem.goal_test(state)

    while not solved:
        print(state)        # show the board
        
        # Generate possible actions and corresponding labels a, b, c
        actions = problem.actions(state)  # what can we do?

        # enumerate choices: a, b, c, ...
        action_labels = [chr(ord('a')+idx) for idx in range(len(actions))]
        # Print list of actions, end="" means no newline
        print("Valid actions (delta row, delta col): ")
        for (label, move) in zip(action_labels, actions):
            print(f"{label}: {move}.  ", end="")
        print()
        
        # Let user select a valid choice
        useraction = None
        prompt = "move choice:  "
        while useraction not in action_labels:
            useraction = input(prompt)
            prompt = "bad choice, try again: "
        print(useraction)
        
        # Convert choice to index and execute move
        actionidx = ord(useraction) - ord('a')
        state = problem.result(state, actions[actionidx])
        
        solved = problem.goal_test(state) # all done?
        
    print("Congratulations, you did it!")
        
        
        
    
if __name__ == '__main__':
    human_player()