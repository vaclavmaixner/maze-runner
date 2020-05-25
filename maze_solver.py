import pprint
import random
from termcolor import colored, cprint
import os
import utils
import time

from random_search import run_random_search
from bfs import run_bfs
from dfs import run_dfs
from dijkstra import run_dijkstra
from greedy import run_greedy
from a_star import run_a_star


class Maze():

    def __init__(self, layout, start, end):
        self.layout = layout
        self.start = start
        self.end = end

        self.setup_start_end()

    def print_maze(self):
        # os.system('cls' if os.name == 'nt' else 'clear')

        for i in range(len(self.layout)):
            for j in range(len(self.layout[0])):
                if self.layout[i][j] == 'X':  # wall
                    cprint('\u2588\u2588', 'grey', end='')
                elif self.layout[i][j] == ' ':    # fresh node
                    cprint('\u2588\u2588', 'white', end='')
                elif self.layout[i][j] == 'S':    # start
                    cprint('\u2588\u2588', 'green', end='')
                elif self.layout[i][j] == 'E':    # end
                    cprint('\u2588\u2588', 'red', end='')
                elif self.layout[i][j] == 'O':    # opened
                    cprint('\u2588\u2588', 'yellow', end='')
                elif self.layout[i][j] == 'P':    # path
                    cprint('\u2588\u2588', 'blue', end='')
            print()
        time.sleep(0.1)

    def setup_start_end(self):
        self.layout[self.start[0]][self.start[1]] = 'S'
        print()
        print(len(self.layout))
        print(len(self.layout[0]))
        print(self.end[0])
        print(self.end[1])

        self.layout[self.end[0]][self.end[1]] = 'E'

    def get_neighbours(self, node):
        x, y = node
        neighbours = [(x, y+1), (x+1, y), (x, y-1), (x - 1, y)]
        return neighbours

    def report(self, name):
        self.print_maze()

        opened_counter = 0
        path_counter = 0

        for i in range(len(self.layout)):
            for j in range(len(self.layout[0])):
                if self.layout[i][j] == 'O':    # opened
                    opened_counter += 1
                elif self.layout[i][j] == 'P':    # path
                    path_counter += 1
        opened_counter += path_counter
        
        print(30 * '-')
        print(name)
        print(30 * '-')
        cprint('\u2588\u2588', 'green', end='')
        print(' Start')
        cprint('\u2588\u2588', 'red', end='')
        print(' End')
        cprint('\u2588\u2588', 'yellow', end='')
        print(' Opened')
        cprint('\u2588\u2588', 'blue', end='')
        print(' Path')
        cprint('\u2588\u2588', 'grey', end='')
        print(' Wall')
        print(30 * '-')
        print('Nodes expanded:', opened_counter)
        print('Path length:', path_counter)



def Main():
    layout = open('testovaci_data/00_11_11_1550177690.txt', 'r')

    pl = utils.process_layout(layout)
    maze = Maze(pl[0], pl[1], pl[2])

    # run_random_search(maze, put_on_a_show=False)
    # run_bfs(maze, put_on_a_show=False)
    # run_dfs(maze, put_on_a_show=False)
    # run_dijkstra(maze, put_on_a_show=False)
    # run_greedy(maze, put_on_a_show=False)
    run_a_star(maze, put_on_a_show=False)


Main()
