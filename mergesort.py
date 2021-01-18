# Name: Na Kim
# Date: 01/7/2021
# Assignment: CS 325 HW 1

# Reference for merge sort :  https://www.geeksforgeeks.org/merge-sort/

def merge_sort(array_list):
    """ this function implements a merge sort to sort an array/vector of integers in ascending order"""
    if len(array_list) > 1:
        # locate the middle point of array
        mid_array = len(array_list) // 2
        # split the array into 2 halves (defined by left and right half)
        left_half = array_list[:mid_array]
        right_half = array_list[mid_array:]
        # call merge sort to sort the left half
        merge_sort(left_half)
        # call merge sort to sort the right half
        merge_sort(right_half)

        i = j = k = 0
        # merge sort: divide and conquer method

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_list[k] = left_half[i]
                i += 1
            else:
                array_list[k] = right_half[j]
                j += 1
            k += 1

        # check to see if any elements were left
        while i < len(left_half):
            array_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array_list[k] = right_half[j]
            j += 1
            k += 1

# open input text file, data.txt, and read file.
with open("data.txt", "r") as infile:
    result = ''
    for line in infile:
        array = (line.strip())
        array = (line.split())
        # first value of line skipped since it is # of of integers needed to be sorted, not needed
        sorted_array = [int(i) for i in array[1:]]
        merge_sort(sorted_array)
        result += ' '.join(str(i) for i in sorted_array) + '\n'

# results outputted to new text file (merge.out)
with open('merge.out', "w") as outfile:
    outfile.write(result)
    outfile.write('\n')
