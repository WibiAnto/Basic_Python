def split(lists):
    mid = len(lists) // 2
    left = lists[:mid]
    right = lists[mid:]
    return left, right


def merge(left, right):
    li = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            li.append(left[i])
            i += 1
        else:
            li.append(right[j])
            j += 1
    while i < len(left):
        li.append(left[i])
        i += 1
    while j < len(right):
        li.append(right[j])
        j += 1
    return li


def merge_sort(lists):
    """
    sorting list ascending order, output: ordered list
    Algorithm:
    Divide : find the midpoint of the list and divide into sublists.
    Conquer: recursively sort the sublist
    Combine: merge the sorted sublist
    """

    if len(lists) <= 1:
        return lists

    left_half, right_half = split(lists)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


larik = [1, 6, 3, 5, 6, 10, 5]
print(merge_sort(larik))
# belum selesai
