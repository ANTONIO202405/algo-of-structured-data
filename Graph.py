# Graph 
class Graph:
    def __init__(self):
        self.adj_list = {}
    def print_graph(self):
        for key, value in self.adj_list.items():
            print(f"{key} : {value}")
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                if v1 in self.adj_list[v2]:
                    self.adj_list[v2].remove(v1)
                if v2 in self.adj_list[v1]:
                    self.adj_list[v1].remove(v2)
            except ValueError:
                pass
            return True
        return False
    def remove_vertex(self, v1):
        if v1 in self.adj_list:
            del self.adj_list[v1]
        for key in self.adj_list.keys():
            if v1 in self.adj_list[key]:
                self.adj_list[key].remove(v1)
        return True


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_edge(1,2)
my_graph.add_edge(2,3)
my_graph.add_edge(1,3)
my_graph.add_edge(1,4)
my_graph.remove_edge(1,2)
my_graph.remove_edge(1,4)
my_graph.remove_vertex(3)
my_graph.print_graph()
