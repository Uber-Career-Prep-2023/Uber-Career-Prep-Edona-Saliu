"""
Time spent: 20 mins

Time complexity: O(n)

Space complexity: O(n)

Algorithm: 
- count all the characters in s and store the counts in a hash map
- check for the values in t in the hash map and decrement their counts
- find the sum the remaining counts in the hash map
- return whether that sum is less than or equal to k and the lengths of the strings are equal

Edge cases: 
- More than one missing number?
- If the missing number is at the start or end
- No missing number?
"""
def KAnagrams(s, t, k):
    s, t = s.replace(" ", ""), t.replace(" ", "")
    s_dict = {}
    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1

    for char in t:
        if char in s_dict and s_dict[char] > 0:
            s_dict[char] -= 1

    return sum(s_dict.values()) <= k and len(s) == len(t)

s, t = "apple", "peach"
k = 2
# print(KAnagrams(s, t, k))
