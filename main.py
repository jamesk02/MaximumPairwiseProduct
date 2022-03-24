"""
Given a sequence of up to 100,000 non-negative integers
Find the maximum pairwise product: the maximum possible valued
that can be obtained by multiplying the integers together

Input format:
The first line contains a single number of at least 2
The second line contains 0-100,000 non-negative integers
"""
import sys

if __name__ == "__main__":
    nums_ln1 = int(input().split()[0])
    nums_ln2 = input().split()

    numbers = []
    for x in range(len(nums_ln2)):
        numbers.append(int(nums_ln2[x]))

    # Main program
    cur_max = -1
    cur_2nd_max = -1

    cur_max_ind = -1

    # first find max
    for i in range(len(numbers)):
        if numbers[i] > cur_max:
            cur_max = numbers[i]
            cur_max_ind = i

    # now find second max
    for i in range(len(numbers)):
        if numbers[i] > cur_2nd_max and i != cur_max_ind:
            cur_2nd_max = numbers[i]

    print(cur_max * cur_2nd_max)
    0