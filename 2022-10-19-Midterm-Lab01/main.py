from UniformCostSearch import UCS
from GreedyBestfirstSearch import GBFS
from AStar import AStar

start = "Arad"
goal = "Bucharest"

print("Uniform Cost Search:")
UCS(start, goal)
print("\n\nGreedy Bestfirst Search:")
GBFS(start, goal)
print("\n\nA*:")
AStar(start, goal)