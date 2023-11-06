# Q1: 
    


# Q2: 


# q3: 
# intervals schedules = [[start, end], ...]
# length = 

# find first time you can schedule a mtg where everyone's free


# print('yo')

# Question 4 of 4
# 0:01:02
# DESC
# HISTORY
# RULES
# README
# SETTINGS
# Codewriting

# You are given an array of integers numbers and a positive integer k. Your task is to count the number of contiguous subarrays within numbers that contains at least k pairs of elements with duplicate values.

# More formally, count the number of contiguous subarrays numbers[i..j] (i ≤ j) for which there are 2 * k elements (with pairwise distinct indices i ≤ i1, j1, i2, j2, ..., ik, jk ≤ j) with each pair having the same value - numbers[i1] = numbers[j1], numbers[i2] = numbers[j2], ..., numbers[ik] = numbers[jk].

# Example

# For numbers = [0, 1, 0, 1, 0] and k = 2, the output should be solution(numbers, k) = 3.

# There are 3 subarrays that satisfy the criteria of containing at least k = 2 pairs of duplicate values:

# numbers[0..3] = [0, 1, 0, 1] with numbers[0] = 0 = numbers[2] and numbers[1] = 1 = numbers[3]
# numbers[1..4] = [1, 0, 1, 0] with numbers[1] = 1 = numbers[3] and numbers[2] = 0 = numbers[4]
# numbers[0..4] = [0, 1, 0, 1, 0] with numbers[0] = 0 = numbers[2], numbers[1] = 1 = numbers[3], and numbers[2] = 0 = numbers[4]
# In each of these subarrays, there is at least one pair of 0s and one pair of 1s.

# For numbers = [2, 2, 2, 2, 2, 2] and k = 3, the output should be solution(numbers, k) = 1.

# There is only 1 applicable subarray numbers[0..5] = [2, 2, 2, 2, 2, 2], which contains at least three pairs of 2s.

# For numbers = [1, 3, 3, 1] and k = 1, the output should be solution(numbers, k) = 4.

# There are 4 subarrays that satisfy the criteria of containing at least k = 1 pair of duplicate values:

# numbers[0..2] = [1, 3, 3]
# numbers[0..3] = [1, 3, 3, 1]
# numbers[1..2] = [3, 3]
# numbers[1..3] = [3, 3, 1]
# In each of these subarrays, there is at least a pair of 3s.

# Input/Output



