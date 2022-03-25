"""
Given a sequence of up to 100,000 non-negative integers
Find the maximum pairwise product: the maximum possible valued
that can be obtained by multiplying the integers together

Input format:
The first line contains a single number of at least 2
The second line contains 0-100,000 non-negative integers

-=-

Since we just want the biggest possible number created from a pair,
we can simply search for the two biggest numbers that have been inputted
"""
import random
import sys

TEST_MODE = True


def fast_pairwise(_numbers):
    # Main program

    # Initialisations
    cur_max = -1
    cur_2nd_max = -1

    # We use this to verify that the 2nd max isn't actually the first max
    # I previously checked if the cur_max != cur_2nd_max, however this would mean
    # that multiple numbers of the same value would be treated as the same which
    # would mean that the 2nd max would be forced to be assigned to a lesser value
    cur_max_ind = -1

    # first find max : O(N)
    for i in range(len(numbers)):
        if numbers[i] > cur_max:
            cur_max = numbers[i]
            cur_max_ind = i

    # now find second max : O(N)
    for i in range(len(numbers)):
        if numbers[i] > cur_2nd_max and i != cur_max_ind:
            cur_2nd_max = numbers[i]

    # Total TC: O(N) + O(N) = O(N)
    return cur_max * cur_2nd_max


def slow_pairwise(_numbers):
    # Main program
    cur_best = 0

    # forwards
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if cur_best < numbers[i] * numbers[j] and i != j:
                cur_best = numbers[i] * numbers[j]

    return cur_best


if __name__ == "__main__":
    if not TEST_MODE:
        # We don't actually care about the first line, assuming all inputs are valid
        input()
        # String input
        nums_raw = input().split()

        # Convert this string array into integers : O(N)
        numbers = []
        for x in range(len(nums_raw)):
            numbers.append(int(nums_raw[x]))

        print(fast_pairwise(numbers))

    while TEST_MODE:
        n = random.randint(2, 100)
        print(n)
        numbers = []

        for i in range(n):
            numbers.append(random.randint(0, 1000))

        fast_res = fast_pairwise(numbers)
        slow_res = slow_pairwise(numbers)

        if fast_res != slow_res:
            print("Error mismatch")
            print("Fast result: ", fast_res)
            print("Slow result: ", slow_res)

            print("Numbers:\n", numbers)

            sys.exit(0)
