#This file is for HW week3
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def IsAnagram(s, t):
    s_dict = {}
    t_dict = {}
    
    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    
    return s_dict == t_dict

s = "anagram"
t = "nagaram"
print(IsAnagram(s, t))


#Given a non-negative integer x, compute and return the square root of x.
#Since the return type is an integer, the decimal digits are truncated, and 
#only the integer part of the result is returned.
def MySqrt(x):
    if x == 0:
        return 0
    
    left = 1
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right
print('square root of 8 is',MySqrt(8))
