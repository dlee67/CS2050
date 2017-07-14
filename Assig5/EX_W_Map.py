#I should burry this and comeback.

class weighted_digraph:

    class __edge(object):

        def __init__(self, to_node, weight):

            self.to_node = to_node

            self.weight = weight

    class __node(object):

        def __init__(self, value):

            self.value = value

            self.edges = []

            self.distance = 0

            self.because = None

        def __str__(self):

            result = str(self.value)

            for edge in self.edges:

                result += "->" + str(edge.to_node.value) + \
                          "(" + str(edge.weight) + ")"

            return (result)

        def add_edge(self, new_edge):

            if not self.is_adjacent(new_edge.to_node):

                self.edges.append(new_edge)

        def remove_edge(self, to_node):

            for edge in self.edges:

                if edge.to_node == to_node:

                    self.edges.remove(edge)

        def is_adjacent(self, node):

            for edge in self.edges:

                if edge.to_node == node:

                    return (True)

            return (False)

    def __init__(self, directed=True):

        self.__nodes = []

        self.__directed = directed

    def __len__(self):

        return (len(self.__nodes))

    def __str__(self):

        result = ""

        for node in self.__nodes:

            result += str(node) + '\n'

        return (result)

    def get_nodes(self):

        return self.__nodes[:]

    def find(self, value):

        for node in self.__nodes:

            if node.value == value:

                return (node)

        return (None)

    def add_nodes(self, nodes):

        for node in nodes:

            self.add_node(node)

    def add_node(self, value):

        if not self.find(value):

            self.__nodes.append(self.__node(value))

    def add_edges(self, edges):

        for edge in edges:

            self.add_edge(edge[0], edge[1], edge[2])

    """ Add an edge between two values. If the nodes
            for those values aren't already in the graph,
            add those. """

    def add_edge(self, from_value, to_value, weight):

        from_node = self.find(from_value)

        to_node = self.find(to_value)

        if not from_node:

            self.add_node(from_value)

            from_node = self.find(from_value)

        if not to_node:

            self.add_node(to_value)

            to_node = self.find(to_value)

        from_node.add_edge(self.__edge(to_node, weight))

        if not self.__directed:

            to_node.add_edge(self.__edge(from_node, weight))

    def remove_edge(self, from_value, to_value, weight):

        from_node = self.find(from_value)

        to_node = self.find(to_value)

        from_node.remove_edge(to_node)

        if not self.directed:

            to_node.remove_edge(from_node)

    def are_adjacent(self, value1, value2):

        return (self.find(value1).is_adjacent(self.find(value2)))

    def why(self, value, start):

        snake_tail = []

        tail = self.find(value)

        snake_tail.append(tail.distance)

        while tail.value != start:

            snake_tail.append(tail.value)

            tail = tail.because

        snake_tail.append(start)

        return snake_tail

    def dijkstra(self, start):

        to_compare = []

        for_unit_test = []

        will_compare = None

        for node in self.__nodes:

            node.distance = float('inf')

            node.because = None

        source = self.find(start)

        source.distance = 0

        to_compare.append(source)

        while to_compare:

            compared_with = float('inf')

            for node in to_compare:

                if node.distance < compared_with:

                    will_compare = node

                    compared_with = node.distance

            to_compare.remove(will_compare)

            for_unit_test.append([will_compare.distance, will_compare.value])

            for edge in will_compare.edges:

                distance_to_compare = edge.weight + will_compare.distance

                if distance_to_compare < edge.to_node.distance:

                    edge.to_node.distance = distance_to_compare

                    edge.to_node.because = will_compare

                    to_compare.append(edge.to_node)

        if not track_prev:

            final_list = []

            for node in for_unit_test:

                if node not in final_list:

                    final_list.append(node)

        else:

            final_list = []

            for node in for_unit_test:

                if node not in final_list:

                    final_list.append(node)

            final_list_how = []

            for node in final_list:

                final_list_how.append(self.why(node[1], start))

            return final_list_how

graph = weighted_digraph()

print(graph)
