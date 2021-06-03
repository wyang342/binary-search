def binary_search(num_to_search, array):
    sorted_array = sorted(array)

    # sets initial index values
    low = 0
    high = len(sorted_array) - 1

    while True:
        # we know num's not found if low becomes greater than high. This is b/c the elif branches will eventually become low > high if num isn't found.
        if low > high:
            break

        # sets the mid value based on high and low
        mid = low + ((high - low) // 2)

        # make comparisons to middle num
        if num_to_search == sorted_array[mid]:
            return mid
        elif num_to_search < sorted_array[mid]:
            high = mid - 1
        elif num_to_search > sorted_array[mid]:
            low = mid + 1

    return -1  # if not found
