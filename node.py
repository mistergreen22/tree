
valid_variant_one = [
    [{'ip': '22.22.22.22'}],
    [{'ip': '23.23.23.23'}, {'ip': '23.23.23.23'}]
]


valid_variant_two = [
    [{'ip': '22.22.22.22'}, {'ip': '23.23.23.23'}],
    [{'ip': '23.23.23.23'}]
]


valid_variant_three = [
    [{'ip': '23.23.23.23'}],
    [{'ip': '23.23.23.23'}, {'ip': '22.22.22.22'}]
]


valid_variant_four = [
    [{'ip': '23.23.23.23'}, {'ip': '22.22.22.22'}],
    [{'ip': '23.23.23.23'}]
]

invalid_variant = [
    [{'ip': '24.24.24.24'}, {'ip': '22.22.22.22'}],
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


def data_to_tree(data):
    root = Node(data, 1)
    for list_in_list, index_for_list in zip(data, range(len(data))):
        outer_node = Node(list_in_list, index_for_list, root)
        root.add_child(outer_node)
        for dict_in_list, index_for_dict in zip(list_in_list, range(len(list_in_list))):
            inner_left_node = Node(dict_in_list, index_for_dict, outer_node)
            outer_node.add_child(inner_left_node)
            for value_in_dict, index_for_value in zip(dict_in_list.values(), range(len(dict_in_list))):
                inner_right_node = Node(value_in_dict, index_for_value, inner_left_node)
                inner_left_node.add_child(inner_right_node)

    return root


def get_sorted_tree_value(tree):
    values = []
    for list_in_list in tree._children:
        for dict_in_list in list_in_list._children:
            for dict_values in dict_in_list._children:
                values.append(dict_values._value)
    return sorted(values)


if __name__ == "__main__":

    assert get_sorted_tree_value(
        data_to_tree(valid_variant_one)) == get_sorted_tree_value(
        data_to_tree(valid_variant_two))
    assert get_sorted_tree_value(
        data_to_tree(valid_variant_one)) == get_sorted_tree_value(
        data_to_tree(valid_variant_three))
    assert get_sorted_tree_value(
        data_to_tree(valid_variant_one)) == get_sorted_tree_value(
        data_to_tree(valid_variant_four))
    assert get_sorted_tree_value(
        data_to_tree(valid_variant_two)) == get_sorted_tree_value(
        data_to_tree(valid_variant_three))
    assert get_sorted_tree_value(
        data_to_tree(valid_variant_two)) == get_sorted_tree_value(
        data_to_tree(valid_variant_four))
    assert get_sorted_tree_value(
        data_to_tree(valid_variant_three)) == get_sorted_tree_value(
        data_to_tree(valid_variant_four))

    assert get_sorted_tree_value(
        data_to_tree(valid_variant_one)) != get_sorted_tree_value(
        data_to_tree(invalid_variant))
