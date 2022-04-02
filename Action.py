from typing import overload


class Action:
    def __init__(self, line: str) -> None:
        line = line.split(":")[1].split(" ")
        self.id = int(line.pop(0))
        self.probs = {}
        for i in range(0,len(line),2):
            self.probs[int(line[i])] = float(line[i+1])
    
    def __str__(self) -> str:
        return f"{self.id}: {self.probs}"
    
    def __eq__(self, __o: object) -> bool:
        if (type(__o) is Action):
            return __o.id == self.id and __o.probs == self.probs
        return False