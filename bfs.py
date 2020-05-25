import utils


def run_bfs(maze, put_on_a_show):
    print('Breadth first search (BFS) chosen.')
    queue = []
    closed = []
    prev = {}

    queue.append(maze.start)

    while queue:
        open_node = queue.pop(0)

        if open_node == maze.end:
            maze = utils.reconstruct_path(maze, prev, maze.start, maze.end)
            maze.report(name='BFS')

            return maze

        neighbours = maze.get_neighbours(open_node)
        for neighbour in neighbours:
            if maze.layout[neighbour[0]][neighbour[1]] != 'X':
                if neighbour not in closed:
                    queue.append(neighbour)
                    closed.append(neighbour)
                    prev[neighbour] = open_node

        closed.append(open_node)
        if open_node != maze.start:
            maze.layout[open_node[0]][open_node[1]] = 'O'

        if put_on_a_show:
            maze.print_maze()