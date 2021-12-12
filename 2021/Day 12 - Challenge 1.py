# Advent of Code 2021
# Day 12: Passage Pathing
# Part One
# Made by Jeffrey Derksen

class Node:

    def __init__(self, name: str, small: bool) -> None:
        self.name = name
        self.small_node = small
        self.connections = []

    def __str__(self) -> str:
        return self.name


def make_paths(start: Node, end: Node, path=[]):

    if start in path and start.small_node:
        return

    path.append(start)

    if start == end:
        total_paths.append(path)
        return path

    paths = [list(path) for _ in range(len(start.connections))]
    for i, next_node in enumerate(start.connections):
        make_paths(next_node, end, paths[i])


nodes = []
with open('./2021/inputs/12.txt') as f:
    input = f.read().splitlines()
    input = [line.split(sep='-') for line in input]

for connection in input:
    nodes_in_connection = []
    for node_string in connection:
        if node_string not in [item.name for item in nodes]:
            node = Node(node_string, node_string.islower())
            nodes.append(node)
        else:
            node = next(x for x in nodes if node_string == x.name)
        nodes_in_connection.append(node)

    nodes_in_connection[0].connections.append(nodes_in_connection[1])
    nodes_in_connection[1].connections.append(nodes_in_connection[0])

start_node = next(x for x in nodes if 'start' == x.name)
end_node = next(x for x in nodes if 'end' == x.name)

total_paths = []
make_paths(start_node, end_node)
print('Total paths:', len(total_paths))
