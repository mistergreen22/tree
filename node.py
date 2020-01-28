expected_result = [
    [{'a': 1}],
    [{'a': 2}, {'a': 1}]
]

actual_result = [
    [{'a': 1}],
    [{'a': 1}, {'a': 2}]
]

more_vars = [
    [{'a': 1}, {'a': 2}],
    [{'a': 1}]
]


class Node:
    def __init__(self, value, index, parent=None):
        self._parent = parent
        self._children = []
        self._value = value
        self._index = index

    def add_child(self, child):
        self._children.append(child)

    def __str__(self):
        return f'{type(self._value)} -> {len(self._children)}'

    def uuid(self):
        return f'{self._value if not len(self._children) else ""}|{self._index}|{self._parent.uuid()}'



def data_to_tree(data):
    root = Node(data, 1)
    for outer_list, my_index in zip(data, range(len(data))):
        outer_node = Node(outer_list, my_index, root)
        root.add_child(outer_node)
        for inner_list, i in zip(outer_list, range(len(outer_list))):
            inner_node = Node(inner_list, i, outer_node)
            root.add_child(inner_node)
            for inner_dict, y in zip(inner_list, range(len(inner_list))):
                dict_node = Node(inner_dict, y, inner_node)
                root.add_child(dict_node)

    return root


if __name__ == "__main__":
    print(data_to_tree(expected_result))
    #assert expected_result == actual_result
