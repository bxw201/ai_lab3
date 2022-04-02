from State import NonterminalState, TerminalState
from Action import Action

class World:
    def __init__(self, fn: str) -> None:
        with open(fn, encoding='utf-8') as f:
            self.process_line1(f.readline()) # first line
            self.process_line2(f.readline()) # second line
            for line in f.readlines():
                self.process_actions(line)

    def __str__(self) -> str:
        ret = f"n: {self.n}, t: {self.t}, rounds: {self.rounds}, print_freq; {self.print_freq}, M: {self.M}"
        for state in self.states:
            ret += "\n" + str(state)
        return ret

    def process_line1(self, line1: str) -> None:
        args = line1.split(" ")
        self.n = int(args[0])
        self.t = int(args[1])
        self.rounds = int(args[2])
        self.print_freq = int(args[3])
        self.M = int(args[4])

        self.states = []
        for i in range(self.n): self.states.append(NonterminalState(i))
        for i in range(self.n, self.n + self.t): self.states.append(TerminalState(i))

    def process_line2(self, line2: str) -> None:
        args = line2.split(" ")
        for i in range(0,len(args),2): 
            assert type(self.states[int(args[i])]) is TerminalState, "Not a terminal state"
            self.states[int(args[i])].add_reward(int(args[i+1]))

    def process_actions(self, action_line: str) -> None:
        self.states[int(action_line[0])].add_action(Action(action_line))
        pass

    def NonterminalStates(self) -> list:
        return self.states[:self.n]

    def TerminalStates(self) -> list:
        return self.states[self.n:]

if __name__ == "__main__":
    W = World("test_input.txt")
    print(W)