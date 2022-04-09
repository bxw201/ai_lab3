'''driver for running through the given input'''

import sys
from os.path import exists
from agent import Agent
from world import World

def run(file_name: str) -> None:
    '''run through the input given in the file_name file
    input: file_name - the name of the file containing the input'''
    world = World(file_name)
    agent = Agent(world)
    agent.run()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please give a file name.")
        sys.exit(1)

    fn = sys.argv[1]

    if not exists(fn):
        print("File does not exist")
        sys.exit(1)

    run(fn)
