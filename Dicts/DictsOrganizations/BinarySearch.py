def BinarySearch(wanted, key_list, return_index=False):
    if len(key_list) == 0 and not return_index:
        return None
    left = 0
    right = len(key_list) - 1
    middle = 0
    while left < right:
        middle = (left + right)//2
        if wanted <= key_list[middle]:
            right = middle
        else:
            left = middle + 1
    if key_list[left] != wanted and not return_index:
        return None
    return left
