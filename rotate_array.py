"""
  Rootate array (LeetCode)
  
  found at:  https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
  
  Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

import math 
class Solution(object):
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length > 1 and k > 0:
            # check whether k is factor of length, or a multiple of one of its factors.
            # If k is a factor of length, or a factor multiple, the loop will start cycling over
            # the same indices at a certain point. This must be avoided
            divcheck = 1
            factor_cycle_length = int(math.lcm(length, k) / k)

            # index that element at current iteration will be moved to
            newpos = 0
            # element that we want to move at current iteration
            curr = nums[newpos]
            # counter used to stop the while loop after visiting the whole array
            loop_iter_count = 0

            while loop_iter_count < len(nums):
                #print("\tcurr", curr, "\tcurrpos", newpos, "\tdivcheck", divcheck)
                # find new position that current element will be moved to
                newpos = (newpos + k) % length
                #print("\t-->newpos", newpos)
                # memorize element currently at newpos
                next = nums[newpos]
                # move current element to newpos
                nums[newpos] = curr
                # update curr
                curr = next
                loop_iter_count += 1

                if factor_cycle_length > 1:
                    if divcheck == factor_cycle_length:
                        # if divcheck == divcount, then you are starting to cycle over an already visited index
                        # to avoid this, increment newpos and reset divcheck
                        newpos += 1
                        divcheck = 0
                        curr = nums[newpos]
                    divcheck += 1
