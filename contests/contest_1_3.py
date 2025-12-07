from collections import defaultdict, deque
import sys


def graph_search_deep(edges, root_vertex):
    visited_vertex = set()
    stack = deque()
    stack.append(root_vertex)
    while stack:
        peek = stack.pop()
        if peek in visited_vertex:
            continue
        print(peek)
        visited_vertex.add(peek)
        if peek in edges.keys():
            ed_ver = edges[peek]
            for i in range(len(ed_ver) - 1, -1, -1):
                stack.append(ed_ver[i])
    return


def graph_search_width(edges, root_vertex):
    visited_vertex = set()
    queue = deque()
    queue.append(root_vertex)
    while queue:
        peek = queue.popleft()
        if peek in visited_vertex:
            continue
        print(peek)
        visited_vertex.add(peek)
        if peek in edges.keys():
            for i in edges[peek]:
                queue.append(i)
    return


graph = defaultdict(list)
graph_type, start_vertex, search_type = sys.stdin.readline().split()
for line in sys.stdin:
    if line.strip() == '':
        break
    ver_start, ver_end = line.split()
    graph[ver_start].append(ver_end)
    if graph_type == 'u':
        graph[ver_end].append(ver_start)
for i in graph.keys():
    graph[i].sort()
if search_type == 'd':
    graph_search_deep(graph, start_vertex)
else:
    graph_search_width(graph, start_vertex)
