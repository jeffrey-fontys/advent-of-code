# Advent of Code 2021
# Day 12: Passage Pathing
# Part Two
# Made by Jeffrey Derksen

class Node:

    def __init__(self, name: str, small: bool) -> None:
        self.name = name
        self.small_node = small
        self.connections = []

    def __str__(self) -> str:
        return self.name


def make_paths(start: Node, end: Node, next: Node,
               allowed_smalls: int, start_allowed: bool = True, path=[]):

    if next in path and next.small_node:
        allowed_smalls -= 1

    if next in path and next.small_node and allowed_smalls < 0 or \
            next == start and not start_allowed:
        return

    path.append(next)

    if next == end:
        total_paths.append(path)
        return path

    paths = [list(path) for _ in range(len(next.connections))]
    for i, next_node in enumerate(next.connections):
        make_paths(start, end, next_node, allowed_smalls, False, paths[i])


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
make_paths(start_node, end_node, start_node, 1)
print('Total paths:', len(total_paths))
