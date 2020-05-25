import random
import utils


def run_random_search(maze, put_on_a_show):
    print('Random search chosen.')
    queue = []
    closed = []
    prev = {}

    queue.append(maze.start)

    while queue:
        open_node = random.choice(queue)

        if open_node == maze.end:
            maze = utils.reconstruct_path(maze, prev, maze.start, maze.end)
            maze.report('Hur dur (Random search)')

            return maze

        neighbours = maze.get_neighbours(open_node)
        for neighbour in neighbours:
            if maze.layout[neighbour[0]][neighbour[1]] != 'X':
                if neighbour not in closed:
                    queue.append(neighbour)
                    prev[neighbour] = open_node

        queue.remove(open_node)
        closed.append(open_node)
        if open_node != maze.start:
            maze.layout[open_node[0]][open_node[1]] = 'O'

        if put_on_a_show:
            maze.print_maze()
