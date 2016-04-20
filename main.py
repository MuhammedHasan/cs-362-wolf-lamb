from game import *
import copy
from idfs import IDFS
from astar import AStar
import time

for algortim in [IDFS, AStar]:
    print algortim.__name__

    timeOfSearch = time.time()
    g = GameState(number_of_animal=3)
    tree = algortim(g)

    solution = None
    while not solution:
        solution = tree.search()

    for i in solution:
        print i

    print 'running time %f' % (time.time() - timeOfSearch)
    print
