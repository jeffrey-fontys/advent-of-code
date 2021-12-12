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


def count_paths(start: Node, end: Node, next: Node,
                allowed_smalls: int, start_allowed: bool = True, visited=[]):

    if next in visited and next.small_node:
        allowed_smalls -= 1

    if next in visited and next.small_node and allowed_smalls < 0 or \
            next == start and not start_allowed:
        return 0

    visited.append(next)

    if next == end:
        return 1

    count = 0
    for next_node in next.connections:
        count += count_paths(start, end, next_node,
                             allowed_smalls, False, list(visited))

    return count


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

total_paths = count_paths(start_node, end_node, start_node, 1)
print('Total paths:', total_paths)
