'''module defines the state and (non)terminal state, a position that an
agent can be in in the world'''

from action import Action

class State:
    '''parent class of both terminal and nonterminal states. has an id'''
    def __init__(self, state_id: int) -> None:
        self.id = state_id

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, State):
            # nonterminal states will never have the same id as terminal states
            return __o.id == self.id
        return False

class TerminalState(State):
    '''represents a terminal state with a reward'''
    def __init__(self, state_id: int) -> None:
        super().__init__(state_id)
        self.reward = 0

    def add_reward(self, reward: int) -> None:
        '''adds a reward to the state
        input: reward - the reward to add'''
        self.reward = reward

    def __str__(self) -> str:
        return f"TerminalState - id: {self.id}, reward: {self.reward}"

class NonterminalState(State):
    '''represents a nonterminal state with multiple actions'''
    def __init__(self, state_id: int) -> None:
        super().__init__(state_id)
        self.actions = []

    def add_action(self, action: Action) -> None:
        '''adds an action to the list of actions
        input: action - the action to add'''
        self.actions.append(action)

    def __str__(self) -> str:
        ret = f"NonterminalState - id: {self.id}"
        for action in self.actions:
            ret += "\n\t" + str(action)
        return ret
