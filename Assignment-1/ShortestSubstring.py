"""
Time spent: 30 mins

Time complexity: O(n)

Space complexity: O(n)

Algorithm: 
- use dictinaries to store an encoding on string by ASCII values of characters
- Have a function to check if the encoding of s encompasses that of t
- Keep track of the shortest length seen so far
- Keep extending the window to the right if you haven't found all chars in t
- Start shrinking the window from the left when you have all required chars in t
and stop when you no longer have any
- Update the minimum length as you shrink the window
- Return the minimum length

Edge cases: 
- What if the data types of s and t are not string?
- Can t be longer than s?
"""
def ShortestSubstring(s, t):
    t_enc = {i:0 for i in range(ord("A"), ord("z")+1)}
    s_enc = {i:0 for i in range(ord("A"), ord("z")+1)}
    
    for char in t:
        t_enc[ord(char)] += 1

    def check_encs(s_enc, t_enc):
        for i in s_enc:
            if t_enc[i] > s_enc[i]:
                return False
        return True

    l = 0
    min_len = len(s)+1
    for r in range(len(s)):
        s_enc[ord(s[r])] += 1
        while check_encs(s_enc, t_enc):
            min_len = min(min_len, r-l+1)
            s_enc[ord(s[l])] -= 1
            l += 1

    return min_len

s, t = "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"
# print(ShortestSubstring(s, t))
