## DFS
### Stack approach
```python
def DFS_stack(graph,start):
    stack = []
    stack.append(start)
    visited = set{}
    visited.add(start)

    while stack != []:
        vertex = stack.pop()
        for item in graph[vertex]:
            if item in visited:
                stack.append(item)
                visited.add(item)
      print (vertex)
```

### Recursion approach
```python
def DFS_recusion(graph,start):
    visited = {node:False for node in list(graph.keys())}

    def DFS(root):
        print (root)
        visited[root] = True
        for item in graph(root):
            if not visited[item]:
                DFS(item)

    DFS(start)
```

### What is the three colors recursive DFS algorithm? Learn it asap.

## BFS
### Queue approach
``` python
def DFS_queue(graph,start):
    queue = []
    queue.append(start)
    visited = set{}
    visited.add(start)

    while queue != []:
        vertex = queue.pop(0)
        for item in graph[vertex]:
            if item in visited:
                queue.append(item)
                visited.add(item)

        print (vertex)
```

## Connected Components
```python
def connectedComponents(graph,start):
    visited = {node:False for node in list(graph.keys())}







```
