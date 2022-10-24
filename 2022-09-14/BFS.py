graph = {
  'a' : ['b','e','f'],
  'b' : ['c','a'],
  'c' : ['f','d','b'],
  'd' : ['g','c'],
  'e' : ['i','a'],
  'f' : ['j','c','a'],
  'g' : ['d','j','k','h'],
  'h' : ['o','g'],
  'i' : ['j','e','m','n'],
  'j' : ['i','g','f'],
  'k' : ['o','g'],
  'm' : ['i'],
  'n' : ['o','i'],
  'o' : ['h','k','p'],
  'p' : ['l'],
  'l' : ['p']
}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Breadth-First Search")
bfs(visited, graph, 'a')