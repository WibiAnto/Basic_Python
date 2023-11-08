def linear_search(list, target):
    """Return the index position of the target if found, else return None"""
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in List")


number = [i for i in range(1,20)]
result = linear_search(number, 5)
verify(result)
