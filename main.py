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
if __name__ == "__main__":
    # We don't actually care about the first line, assuming all inputs are valid
    input()
    # String input
    nums_raw = input().split()

    # Convert this string array into integers : O(N)
    numbers = []
    for x in range(len(nums_raw)):
        numbers.append(int(nums_raw[x]))

    numbers = [0] * 100000

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

    print(cur_max * cur_2nd_max)

    # Total TC: O(N) + O(N) + O(N) = O(N)
