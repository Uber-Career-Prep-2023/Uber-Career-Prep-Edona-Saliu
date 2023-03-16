"""
Time spent: 10 mins

Time complexity: O(n)

Space complexity: O(n)

Algorithm: 
- loop through the characters in the string and save their locations
and characters in different lists
- reverse the list with locations
- Map the vowels to the reversed locations
- Return the string after joining in back from it's list form

Edge cases: 
- 
"""
def ReverseVowels(s):
    vowels = []
    vowel_locs = []
    s_lst = list(s)
    v = set(["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"])
    for i, char in enumerate(s):
        if char in v:
            vowels.append(char)
            vowel_locs.append(i)

    vowel_locs = vowel_locs[::-1]
    for i in range(len(vowel_locs)):
        s_lst[vowel_locs[i]] = vowels[i]

    return "".join(s_lst)