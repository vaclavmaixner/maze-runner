import utils


def run_dijkstra(maze, put_on_a_show):
    print('Dijkstra chosen.')
    queue = []
    prev = {}
    distance = {}

    queue.append(maze.start)
    distance[maze.start] = 0

    while queue:
        open_node = queue.pop(0)

        if open_node == maze.end:
            maze = utils.reconstruct_path(maze, prev, maze.start, maze.end)
            maze.report(name='Dijkstra')

            return maze

        neighbours = maze.get_neighbours(open_node)
        for neighbour in neighbours:
            distance_to_node = distance[open_node] + utils.get_distance(open_node, neighbour)
            if maze.layout[neighbour[0]][neighbour[1]] != 'X':
                if (neighbour not in distance.keys()) or (distance_to_node < distance[neighbour]):
                    queue.append(neighbour)
                    
                    prev[neighbour] = open_node
                    distance[neighbour] = distance_to_node

        if open_node != maze.start:
            maze.layout[open_node[0]][open_node[1]] = 'O'

        if put_on_a_show:
            maze.print_maze()