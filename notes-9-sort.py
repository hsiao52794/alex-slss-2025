# Intro to Sort
# Author: Alex
# 4 December

import csv

# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order

def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort

    params:
        l - list of numbers to sort
        ascending - rue if sorting in ascending order

    returns:
        a sorted list

    """

    num_items = len(l)
    for i in range(num_items):
        lowest_num = l[i]
        lowest_index = i

        # check the rest of the list
        for j in range(i+1, num_items):
            if l[j] < lowest_num:
                lowest_num = l[j]
                lowest_index = j
            # go to the next num until we get to the end
        l[i], l[lowest_index] = l[lowest_index], l[i]

    return l

if __name__ == "__main__":
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34])

    print(sorted_list)
