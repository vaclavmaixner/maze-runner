import utils
import heapq


def run_greedy(maze, put_on_a_show):
    print('Greedy search chosen.')
    queue = []
    closed = []
    prev = {}

    # queue.append(maze.start)
    heapq.heappush(queue, (0, maze.start))

    while queue:
        # open_node = queue.pop(0)
        open_node = heapq.heappop(queue)[1]

        if open_node == maze.end:
            maze = utils.reconstruct_path(maze, prev, maze.start, maze.end)
            maze.report(name='Greedy search')

            return maze

        neighbours = maze.get_neighbours(open_node)
        for neighbour in neighbours:
            dist_to_end = utils.get_distance(neighbour, maze.end)
            if maze.layout[neighbour[0]][neighbour[1]] != 'X':
                if neighbour not in closed:
                    # queue.append(neighbour)
                    heapq.heappush(queue, (dist_to_end, neighbour))

                    closed.append(neighbour)
                    prev[neighbour] = open_node

        closed.append(open_node)
        if open_node != maze.start:
            maze.layout[open_node[0]][open_node[1]] = 'O'

        if put_on_a_show:
            maze.print_maze()
