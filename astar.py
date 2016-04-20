import copy
from idfs import IDFS
import math


class AStar(IDFS):
    ''' A* Search '''

    def expand(self):
        end_children = self.end_children()
        self.limit += 1
        for i in end_children:
            i.cost = self.limit
        self.expand_nodes(
            [max(
                end_children,
                key=lambda x: x.cost + self.heuristic_of_node(x)
            )]
        )

    def heuristic_of_node(self, node):
        h = abs(node.sheepDown - node.wolfDown)
        h += abs(node.sheepUp - node.wolfUp)
        return 2 * (node.sheepUp + node.wolfUp) - h
