'''module contains the Agent class, representing the agent going through a
given world model'''

import random
from action import Action
from state import State, TerminalState
from world import World

class Agent:
    '''represents agent learning the best policy to traverse the world model'''

    def __init__(self, world: World) -> None:
        self.world = world
        self.count = [[0] * len(s.actions) for s in world.nonterminal_states()]
        self.total = [[0] * len(s.actions) for s in world.nonterminal_states()]

    def run(self) -> None:
        '''run a simulation through the world for multiple rounds,
        incrementing count and total according to the
        choices made and the end result of each round.
        print the current status every v rounds'''
        for i in range(1, self.world.rounds + 1):
            self.run_round()
            if i % self.world.v == 0:
                self.print_round(i)

        if self.world.rounds % self.world.v != 0:
            self.print_round(self.world.rounds)
        self.reset()

    def reset(self) -> None:
        '''reset the agent for another round through the world'''
        self.count = [[0] * len(s.actions) for s in self.world.nonterminal_states()]
        self.total = [[0] * len(s.actions) for s in self.world.nonterminal_states()]

    def run_round(self) -> None:
        '''run one round through the world from a random nonterminal state
        until hitting a terminal state. increment total by the value of the
        terminal state'''
        cur = random.choice(self.world.nonterminal_states())
        visited = [] # list of tuples of (state, action taken at state)

        while not isinstance(cur, TerminalState):
            action = self.choose_action(cur)
            visited.append((cur, action))
            cur = self.world.states[action.pick_state()[0]]

        for (state, action) in visited:
            self.count[state.id][action.id] += 1
            self.total[state.id][action.id] += cur.reward

    def choose_action(self, state: State) -> Action:
        '''given a state, return an action to take based on the
        algorithm given in the specs
        input: state - the state to pick an action from
        return Action - the action picked from state'''
        if isinstance(state, TerminalState):
            return None
        num_actions = len(state.actions)
        for i in range(num_actions):
            if self.count[state.id][i] == 0:
                return state.actions[i]
        avg = [self.total[state.id][i]/self.count[state.id][i] for i in range(num_actions)]
        bottom = min(avg)
        top = max(avg)
        if top == bottom:
            # all actions as good as each other
            return random.choices(state.actions)[0]
        savg = [.25 + .75*(avg[i] - bottom)/(top - bottom) for i in range(num_actions)]
        c = sum(self.count[state.id])
        up = [i**(c/self.world.M) for i in savg]
        norm = sum(up)
        p = [i/norm for i in up]
        return random.choices(state.actions, weights=p)[0]

    def print_count(self) -> None:
        '''print the current state of the count array'''
        print("Count:")
        for (i, state) in enumerate(self.count):
            for (j, _) in enumerate(state):
                print(f"[{i},{j}]={self.count[i][j]}. ", end="")
            print()

    def print_total(self) -> None:
        '''print the current state of the total array'''
        print("\nTotal:")
        for (i, state) in enumerate(self.total):
            for (j, _) in enumerate(state):
                print(f"[{i},{j}]={self.total[i][j]}. ", end="")
            print()

    def best_action(self, state: State) -> Action:
        '''given a state, pick the best action based on the
        average total of running that action
        input: state - the state to pick the best action from
        return Action - the best action
                        None if there's an action that's never been tried'''
        if 0 in self.count[state.id]:
            return None
        avg = [self.total[state.id][i]/self.count[state.id][i] for i in range(len(state.actions))]
        return state.actions[avg.index(max(avg))]

    def print_best_action(self, state: State) -> None:
        '''given a state, print the best action based on self.best_action
        input: state - the state to print the best action from'''
        best = self.best_action(state)
        best_str = "U" if best is None else best.id
        print(f"{state.id}:{best_str}", end=" ")

    def print_round(self, round_num: int) -> None:
        '''print the current state of the agent
        input: round_num - the number of rounds already run'''
        print(f"After {round_num} rounds")
        self.print_count()
        self.print_total()
        print("\nBest action:", end=" ")
        for state in self.world.nonterminal_states():
            self.print_best_action(state)
        print("\n\n=========================\n")

if __name__ == "__main__":
    W = World("test_input2.txt")
    A = Agent(W)
    A.run()
