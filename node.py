expected_result = [
    [{'a': 1212}],
    [{'a': 2121}, {'a': 1212}]
]

actual_result = [
    [{'a': 1}],
    [{'a': 1}, {'a': 2}]
]

more_vars = [
    [{'ip': '22.22.22.22'}, {'ip': '23.23.23.23'}],
    [{'ip': '23.23.23.23'}]
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
        return f'{self._value if not len(self._children) else ""}|{self._index}| {self._parent.uuid() if self._parent is not None else ""}'

    def __eq__(self, other):
        if self.uuid() == other.uuid() and sorted(self._children) == sorted(other._children):
            return True
        else:
            return False


def data_to_tree(data):
    root = Node(data, 1)
    for list_in_list, index_for_list in zip(data, range(len(data))):
        outer_node = Node(list_in_list, index_for_list, root)
        root.add_child(outer_node)
        for dict_in_list, index_for_dict in zip(list_in_list, range(len(list_in_list))):
            inner_left_node = Node(dict_in_list, index_for_dict, outer_node)
            root.add_child(inner_left_node)
            for value_in_dict, index_for_value in zip(dict_in_list.values(), range(len(dict_in_list))):
                inner_right_node = Node(value_in_dict, index_for_value, inner_left_node)
                root.add_child(inner_right_node)

    return root


if __name__ == "__main__":

    print(data_to_tree(more_vars))
    var = data_to_tree(more_vars)
    var2 = var.uuid()
    print(var2)
    print(data_to_tree(expected_result).uuid() == data_to_tree(actual_result).uuid())
    #assert expected_result == actual_result
