from __future__ import annotations

import logging
from collections import deque
from itertools import permutations

from .euler.sequence.polygonal import Triangle, Square, Pentagonal, Hexagonal, Heptagonal, Octagonal, Polygonal
from .euler.util.decorators import timed_function


class PolygonalNode:
    def __init__(self, polygonal_degree: int, number: int):
        self.polygonal_degree = polygonal_degree
        self.number = number

        number_string = str(number)
        self.prefix = number_string[:len(number_string) // 2]
        self.suffix = number_string[len(number_string) // 2:]

        self.connected = []

    def add_connection(self, node: PolygonalNode):
        if self.is_connected(node):
            self.connected.append(node)

    def is_connected(self, node: PolygonalNode):
        return self.suffix == node.prefix

    def __str__(self):
        return f'[{self.polygonal_degree}]({self.number})'

    def can_form_cycle_with(self, path: [PolygonalNode]):
        return all(self.polygonal_degree != node.polygonal_degree for node in path)


def generate_polygonal_nodes(polygon_type: Polygonal, digits: int):
    return [
        PolygonalNode(polygon_type.polygonal_degree, number)
        for number in polygon_type.generate_numbers_with(digits)
    ]


def connect_nodes_in_graph(graph: [[PolygonalNode]]):
    for collection1, collection2 in permutations(graph, 2):
        for node1 in collection1:
            for node2 in collection2:
                node1.add_connection(node2)


def find_cyclical_figurate_number(graph: [[PolygonalNode]]):
    paths = deque([([node], node) for node in graph[-1]])
    while paths:
        path, last_node_in_path = paths.pop()
        for connected_node in last_node_in_path.connected:
            if connected_node.can_form_cycle_with(path):
                if len(path) == 5:
                    if connected_node.is_connected(path[0]):
                        logging.debug([(node.polygonal_degree, node.number) for node in path + [connected_node]])
                        return sum([node.number for node in path + [connected_node]])

                    continue

                paths.append((path + [connected_node], connected_node))


def q61(digits=4):
    polygonal_sequence_types = [Triangle(), Square(), Pentagonal(), Hexagonal(), Heptagonal(), Octagonal()]
    all_polynomial_numbers_in_range = [generate_polygonal_nodes(polygonal_sequence_type, digits)
                                       for polygonal_sequence_type in polygonal_sequence_types]

    connect_nodes_in_graph(all_polynomial_numbers_in_range)
    return find_cyclical_figurate_number(all_polynomial_numbers_in_range)


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(Triangle.to_index)(Triangle(), 10 ** 3) == 44.224154547626725)

    assert (timed_function(q61)() == 28684)
