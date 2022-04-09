'''module contains action class, representing an action to
be taken by an agent at a certain state'''

import random

class Action:
    '''an action that can be taken by a certain state
    gives the probability of moving to each state if taking the action in self.probs'''
    def __init__(self, line: str) -> None:
        line = line.strip().split(":")[1].split(" ")
        self.id = int(line.pop(0))
        self.probs = {}
        for i in range(0,len(line),2):
            self.probs[int(line[i])] = float(line[i+1])

    def pick_state(self) -> int:
        '''returns int - the id of the state to move to if this action is taken'''
        possible_states = list(self.probs.keys())
        state_probs = list(self.probs.values())
        return random.choices(possible_states, weights=state_probs)

    def __str__(self) -> str:
        return f"{self.id}: {self.probs}"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Action):
            return __o.id == self.id and __o.probs == self.probs
        return False
