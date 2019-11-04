import collections


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


def bfs(vertex_info):
    q = collections.deque()
    visited = set()
    initial_vertex = set(vertex_info.keys()).pop()

    q.append(initial_vertex)

    while len(q) is not 0:

        vertex = q.popleft()
        print(vertex, end=" ")
        visited.add(vertex)
        for child in vertex_info[vertex].child:
            if child not in visited and child not in q:
                q.append(child)


vertex_info = make_graph(edges)

print(vertex_info)

bfs(vertex_info)
