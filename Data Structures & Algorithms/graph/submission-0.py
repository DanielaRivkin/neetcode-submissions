class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []
        self.adjList[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True  # Successfully removed
        return False  # Edge does not exist

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False  # If either node is missing, no path exists

        stack = [src]
        visited = set()

        while stack:
            node = stack.pop()
            if node == dst:
                return True  # Found the destination

            if node not in visited:
                visited.add(node)
                stack.extend(self.adjList.get(node, []))  # Add neighbors to stack

        return False  # No path found
