from d_linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sort linked list in ascending order
    Algorithm:
    - Divide the linked list into sublist containing a single node
    - Merge the sublist to produce sorted sublist until one remains
    return the sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)
def split(linked_list):
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half,right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
def merge(left, right):
    merged = LinkedList()
    current = merged.head
    left_head = left.head
    right_head = right.head
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node