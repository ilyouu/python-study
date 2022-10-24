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

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Depth-First Search")
dfs(visited, graph, 'a')