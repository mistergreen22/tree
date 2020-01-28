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
    def __init__(self, child, value, parent=None):
        self.parent = parent
        self.child = child
        self.value = value

# Create Node() obj
# format output f''
# triple lvl of nesting using for
# compare structure

    def __str__(self):
        return f''
        pass

    def __eq__(self, other):
        pass


def important_method_for_someth():
    pass


if __name__ == "__main__":
    assert expected_result == actual_result
