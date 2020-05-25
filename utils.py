import math


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

    start = (start[1], start[0])
    end = (end[1], end[0])
    print('Processing the input layout, start is at',
          start, ', end is at ', end, '. ', end='')

    maze_lines = lines[:-2]

    maze = []
    for maze_line in maze_lines:
        maze_line = split_by_char(maze_line)
        maze.append(maze_line)

    return maze, start, end


def reconstruct_path(maze, prev, start, end):
    node = end

    path = []

    while node != start:
        path.append(node)
        node = prev[node]

    path.append(start)

    path.reverse()
    print('The path the algorithm took: ', path, '.')

    for node in path:
        if node != start and node != end:
            maze.layout[node[1]][node[0]] = 'P'

    return maze


def get_distance(open_node, neighbour):
    dy = neighbour[0] - open_node[0]
    dx = neighbour[1] - open_node[1]
    return math.sqrt(dx**2 + dy**2)
