"""
Time spent: 5 mins

Time complexity: O(n)

Space complexity: O(n)

Algorithm: 
- Have empty lists for s and t's chars
- if you see a #, delete the last letter in the list (if there is one)
- if you don't see a #, append it to the list
- compare the two list together 

Edge cases: 
- What if the data types of s and t are not string?
"""
def BackspaceStringCompare(s, t):
    new_s, new_t = [], []
    for char in s:
        if char == "#" and new_s:
            new_s.pop()
        elif char != "#":
            new_s.append(char)

    for char in t:
        if char == "#" and new_t:
            new_t.pop()
        elif char != "#":
            new_t.append(char)

    return "".join(new_s) == "".join(new_t)

s, t = "abcdef###xyz", "abcw#xyz"
# print(BackspaceStringCompare(s, t))