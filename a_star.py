import utils
import heapq


def run_a_star(maze, put_on_a_show):
    print('A* chosen.')
    queue = []
    closed = []
    prev = {}
    distance = {}

    # queue.append(maze.start)
    heapq.heappush(queue, (0, maze.start))
    distance[maze.start] = 0

    while queue:
        # open_node = queue.pop(0)
        open_node = heapq.heappop(queue)[1]

        if open_node == maze.end:
            maze = utils.reconstruct_path(maze, prev, maze.start, maze.end)
            maze.report(name='A*')

            return maze

        neighbours = maze.get_neighbours(open_node)
        for neighbour in neighbours:
            if neighbour not in closed:
                distance_to_node = distance[open_node] + utils.get_distance(open_node, neighbour)
                distance_to_end = utils.get_distance(neighbour, maze.end)
                if maze.layout[neighbour[0]][neighbour[1]] != 'X':
                    if (neighbour not in queue) or (distance_to_node < distance[neighbour]):
                        prev[neighbour] = open_node
                        distance[neighbour] = distance_to_node

                        if neighbour not in queue:
                            heapq.heappush(queue, (distance_to_node + distance_to_end, neighbour))
                        closed.append(neighbour)

        closed.append(open_node)
        if open_node != maze.start:
            maze.layout[open_node[0]][open_node[1]] = 'O'

        if put_on_a_show:
            maze.print_maze()