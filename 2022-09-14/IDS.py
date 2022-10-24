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

path = list()

def DFS(currentNode,destination,graph,maxDepth,curList):
    print("Dang kiem tra den diem ",currentNode)
    curList.append(currentNode)
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,graph,i,curList):
            return True
    return False

if not iterativeDDFS('a','l',graph,12):
    print("No")
else:
    print("Ok")
    print(path.pop())