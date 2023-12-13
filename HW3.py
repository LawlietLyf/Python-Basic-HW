#This file is for Homework in week 4
#Author: Yifu Liu 2101111263

#Q1
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach 
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

def uniquePaths(m, n):
    # 创建一个二维数组来存储路径数量
    dp = [[1] * n for _ in range(m)]

    # 从第二行和第二列开始计算路径数量
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # 最右下角的值即为从左上角到右下角的唯一路径数量
    return dp[-1][-1]

# Test
m = 3
n = 7
result = uniquePaths(m, n)
print("唯一路径数量:", result)


#Q2
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no 
# elements without changing the order of the remaining elements. For example, [3,6,2,7] is a 
# subsequence of the array [0,3,1,6,2,2,7].
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # 初始化dp数组，每个元素至少有一个长度为1的子序列

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

#Test
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
result1 = lengthOfLIS(nums1)
print("最长递增子序列长度:", result1)

nums2 = [0, 1, 0, 3, 2, 3]
result2 = lengthOfLIS(nums2)
print("最长递增子序列长度:", result2)
