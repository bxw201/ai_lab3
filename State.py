from Action import Action

class State:
    def __init__(self, id: int) -> None:
        self.id = id

class TerminalState(State):
    def __init__(self, id: int) -> None:
        super().__init__(id)
    
    def add_reward(self, reward: int) -> None:
        self.reward = reward

    def __str__(self) -> str:
        return f"TerminalState - id: {self.id}, reward: {self.reward}"

class NonterminalState(State):
    def __init__(self, id: int) -> None:
        super().__init__(id)
        self.actions = []
    
    def add_action(self, action: Action) -> None:
        self.actions.append(action)

    def __str__(self) -> str:
        ret = f"NonterminalState - id: {self.id}"
        for action in self.actions:
            ret += "\n\t" + str(action)
        return ret