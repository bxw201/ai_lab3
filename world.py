'''module contains the world class which contains all the relevant
information needed to traverse through the problem'''

from state import NonterminalState, TerminalState
from action import Action

class World:
    '''represents the world in which the agent makes decisions in
    contains information given from the input'''
    def __init__(self, fname: str) -> None:
        with open(fname, encoding='utf-8') as file:
            self.process_line1(file.readline().strip()) # first line
            self.process_line2(file.readline().strip()) # second line
            for line in file.readlines():
                if len(line) <= 1:
                    break
                self.process_actions(line.strip())

    def __str__(self) -> str:
        ret = f"n: {self.n}, t: {self.t}, rounds: {self.rounds}, v; {self.v}, M: {self.M}"
        for state in self.states:
            ret += "\n" + str(state)
        return ret

    def process_line1(self, line1: str) -> None:
        '''stores the information from line one of the file
        inputs: line1 - the first line of the file'''
        args = line1.split(" ")
        self.n = int(args[0])
        self.t = int(args[1])
        self.rounds = int(args[2])
        self.v = int(args[3])
        self.M = int(args[4])

        self.states = []
        for i in range(self.n):
            self.states.append(NonterminalState(i))
        for i in range(self.n, self.n + self.t):
            self.states.append(TerminalState(i))

    def process_line2(self, line2: str) -> None:
        '''stores the information from line two of the file
        inputs: line2 - the second line of the file'''
        args = line2.split(" ")
        for i in range(0,len(args),2):
            assert isinstance(self.states[int(args[i])], TerminalState), "Not a terminal state"
            self.states[int(args[i])].add_reward(int(args[i+1]))

    def process_actions(self, action_line: str) -> None:
        '''stores the information from the file under line two
        inputs: action_line - the line containing the information for an action'''
        self.states[int(action_line[0])].add_action(Action(action_line))

    def nonterminal_states(self) -> list:
        '''returns list[State] - a list of nonterminal states in the world'''
        return self.states[:self.n]

    def terminal_states(self) -> list:
        '''returns list[State] - a list of terminal states in the world'''
        return self.states[self.n:]

if __name__ == "__main__":
    W = World("test_input.txt")
    print(W)
