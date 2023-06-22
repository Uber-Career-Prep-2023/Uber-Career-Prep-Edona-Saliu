"""
Question 7: ReverseWords
Given a string, return the string with the order of the space-separated words reversed

"""

"""
Time complexity: O(N)
Space complexity: O(N)
Time spent: 4 mins
"""

def rev_words(sentence):
    words = sentence.split(" ")
    return " ".join(words[::-1])

rev_words("Emma lives in Brooklyn, New York.")