def recursive_binary(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary(list[midpoint + 1:], target)
            else:
                return recursive_binary(list[:midpoint], target)


def verify(result):
    print(f"Target found: {result}")


number = [i for i in range(1, 20)]
result = recursive_binary(number, 5)
verify(result)
