'''
Time spent: 25 mins
Approach: DP
Time Complexity: O(n^2)
Space Complexity: O(n)
'''

def wordBreak(wrd, dict):
    cache = [False] * (len(wrd) + 1)
    cache[0] = True

    for i in range(1, len(wrd) + 1):
        for j in range(i):
            if cache[j] and wrd[j:i] in dict:
                cache[i] = True
                break
    return cache[-1]

# Test case 1
word_1 = "leetcode"
word_dict_1 = ["leet", "code"]
print(wordBreak(word_1, word_dict_1))  # Should output True (can be broken as "leet code")

# Test case 2
word_2 = "applepenapple"
word_dict_2 = ["apple", "pen"]
print(wordBreak(word_2, word_dict_2))  # Should output True (can be broken as "apple pen apple")

#related test cases from the homework
print(wordBreak("quipig", {"Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"}))
print(wordBreak("mangolf", {"Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"}))
print(wordBreak("manateenotelf", {"Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"}))