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
        self._childred = []
        self._value = value
        self._index = index
# Create Node() obj
# format output f''
# triple lvl of nesting using for
# compare structure

    def add_child(self, child):
        self._childred.append(child)





    def __str__(self):
        return f'{type(self._value)} -> {len(self._childred)}'

    def uuid(self):
        return f'{self._value if not len(self._childred) else ""}|{self._index}|{self._parent.uuid()}'



def data_to_tree(data):
    root = Node(data, 1)
    for my_list, my_index in zip(data, range(len(data))):
        var = Node(my_list, my_index, root)
        root.add_child(var)
        for sec_list, 
    #.....

    return root


def important_method_for_someth():
    pass


if __name__ == "__main__":
    assert expected_result == actual_result
