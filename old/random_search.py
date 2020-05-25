import pprint
import random
from termcolor import colored, cprint
import os


layout = open('vstup.txt', 'r')


def print_maze(maze):
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'X':
                cprint('\u2588\u2588', 'grey', end='')
            elif maze[i][j] == ' ':
                cprint('\u2588\u2588', 'white', end='')
            elif maze[i][j] == 'S':
                cprint('\u2588\u2588', 'green', end='')
            elif maze[i][j] == 'E':
                cprint('\u2588\u2588', 'red', end='')
            elif maze[i][j] == 'O':
                cprint('\u2588\u2588', 'yellow', end='')
            elif maze[i][j] == 'P':
                cprint('\u2588\u2588', 'blue', end='')
        print()


def split_by_char(line):
    return [char for char in line]


def process_layout(layout):
    lines = []
    for line in layout:
        line = line.replace('\n', '')
        lines.append(line)

    start_line = lines[-2:-1][0].replace(',', '')
    end_line = lines[-1:][0].replace(',', '')

    start = [int(s) for s in start_line.split() if s.isdigit()]
    end = [int(s) for s in end_line.split() if s.isdigit()]
    print('Processing the input layout, start is at', start, ', end is at ', end)

    maze_lines = lines[:-2]

    maze = []
    for maze_line in maze_lines:
        maze_line = split_by_char(maze_line)
        maze.append(maze_line)

    print('The maze looks like this: ')
    pprint.pprint(maze)
    print()

    return maze, start, end


# def get_steps():
#     i_step = random.randint(-1, 1)
#     j_step = random.randint(-1, 1)


def get_neighbours(open_node, maze):
    x, y = open_node[0], open_node[1]
    # print('getting neigbours ', i, j)

    # while True:
    #     i_step = random.randint(-1, 1)
    #     j_step = random.randint(-1, 1)

    #     if i_step != 0 or j_step != 0:
    #         break

    for i in range(-1, 2):
        for j in range(-1, 2):
            if maze[x+i][y+j] == 'X':
                print('X', i, j)

    return open_node[0] + i_step, open_node[1] + j_step


def run_random_search(maze, start, end):
    open_nodes = []
    closed_nodes = []
    previous_nodes = []

    open_nodes.append(start)

    while open_nodes:
        open_node = random.choice(open_nodes)

        if open_node == end:
            return previous_nodes
        print(open_node)

        for i in range(0, 10):
            neighbour = get_neighbours(open_node=open_node, maze=maze)
            print(neighbour)
        open_nodes.pop()

    print_maze(maze)


def Main():
    maze, start, end = process_layout(layout)
    run_random_search(maze, start, end)


# print('\033[94m')
# print('\u2588')

# print('\033[92m')
# print('\u2588')
Main()
