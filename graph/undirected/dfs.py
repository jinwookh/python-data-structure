
class Vertex:
    def __init__(self, data):
        self.child = set()
        self.data = data

    def add_child(self, data):
        self.child.add(data)

    def __repr__(self):
        return str(self.data) + " " + str(self.child)


edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]]


def make_graph(edges):
    vertex_datas = set()
    vertex_with_data = {}

    for edge in edges:
        for vertex in edge:
            vertex_datas.add(vertex)

    for data in vertex_datas:
        vertex_with_data[data] = Vertex(data)

    for edge in edges:
        vertex_with_data[edge[0]].add_child(edge[1])
        vertex_with_data[edge[1]].add_child(edge[0])

    return vertex_with_data


def recursive_dfs(vertex, visited, vertex_info):
    visited[vertex] = True
    print(vertex, end=" ")
    for child in vertex_info[vertex].child:
        if child not in visited.keys():
            recursive_dfs(child, visited, vertex_info)


def dfs(vertex_info):
    vertexes = set(vertex_info.keys())
    initial_vertex = vertexes.pop()

    stack = [initial_vertex]
    visited = []

    while len(stack) is not 0:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.append(vertex)

        for child in vertex_info[vertex].child:
            if child not in visited:
                stack.append(vertex)
                stack.append(child)
                break


vertex_info = make_graph(edges)

print(vertex_info)
random_vertex = set(vertex_info.keys()).pop()

recursive_dfs(random_vertex, {}, vertex_info)
print()
dfs(vertex_info)
