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
    cur_best = 0
    a_i_index = -1
    a_j_index = -1

    # forwards
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if cur_best < numbers[i] * numbers[j] and i != j:
                cur_best = numbers[i] * numbers[j]

    print(cur_best)
    0