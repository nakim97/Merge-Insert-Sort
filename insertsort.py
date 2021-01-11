# Name: Na Kim
# Date: 01/7/2021
# Assignment: CS 325 HW 1

# Reference: Insertion Sort method implemented from CS162 Lecture (Exploration:Searching,sorting,algorithm analysis)

def insert_sort(array_list):
    """ this function will sort a given vector/array of integers in ascending order"""
    # the second value from the array is pulled, values larger than value pulled is slided over, value pulled fills spot
    for index in range(1, len(array_list)):
        val = array_list[index]
        j = index - 1
        # iterate through the array until all values are sorted in correct position
        while j >= 0 and array_list[j] > val:
            array_list[j + 1] = array_list[j]
            j -= 1
        array_list[j + 1] = val

# open input text file, data.txt, and read file.
with open("data.txt", "r") as infile:
    result = ''
    for line in infile:
        array = (line.strip())
        array = (line.split())
        # first value of line skipped since it is # of of integers needed to be sorted, not needed
        sorted_array = [int(i) for i in array[1:]]
        insert_sort(sorted_array)
        result += ' '.join(str(i) for i in sorted_array) + '\n'

# results outputted to new text file (insert.out)
with open('insert.out', "w") as outfile:
    outfile.write(result)
    outfile.write('\n')