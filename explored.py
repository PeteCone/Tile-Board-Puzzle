'''
Created on Feb 8, 2018

@author: mroch
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "init() - Create an empty explored set"
        self.hashmap = dict()

    def exists(self, state):
        """
        exists(state) - Has this state already been explored?
        :param state:  Hashable problem state
        :return: True if already seen, False otherwise
        """
        try:
            return state in self.hashmap[hash(state)]
        except KeyError:
                return False
        return state in self.hashmap[hash(state)]

    def add(self, state):
        """
        add(state) - Add a given state to the explored set
        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """
        if hash(state) not in self.hashmap.keys():
            self.hashmap[hash(state)] = set()
        self.hashmap[hash(state)].add(state)

        """self.__hash__(state)

        self.explored.add(state)
        self.addState = str(state)
        self.explored[self.addState] = True"""



