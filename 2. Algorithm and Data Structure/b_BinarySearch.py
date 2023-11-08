def binary_search(list, target):
    """
    Breaking the array or list down into smaller
    Then find value that targeted
    Weakness: List must be sorted
    """

    first = 0
    last = len(list) - 1
    while first <= last:
        """Binary search algorithm"""
        midpoint = (first + last) // 2  # Floor division
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in List")


number = [i for i in range(1, 20)]
result = binary_search(number, 5)
verify(result)
