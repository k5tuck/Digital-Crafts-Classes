import math

# 1. Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
# nums = [1, 0, 3, 0, 5, 2, 3]
# zero_list = []


# def move_zero(list):
#     for i in list:
#         if i == 0:
#             list.remove(i)
#             zero_list.append(0)
#     list.extend(zero_list)
#     print(list)


# move_zero(nums)

# 2. Write a function that counts the number of times the number 7 occurs in a given integer
# without converting it to a string.
# For example the number 7,704,793 would output 3

# count = 0
# for i in num:
#     if i == "7":
#         count += 1
# print(count)
#
num = 7704793777


def countseven(number):
    count = 0
    while number > 0:
        if number % 10 == 7:
            count += 1
        number = math.floor(number / 10)
    print(count)


countseven(num)
# 3. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Examples and clarification here: https://leetcode.com/problems/two-sum/
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Because nums[0] + nums[1] == 9, we return [0, 1].

# JEREMY'S CHALLENGE:
# 4. You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
# For
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# the output should be
# rotateImage(a) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]