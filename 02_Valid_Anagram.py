'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''
from collections import defaultdict
def isAnagram(s, t):
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    for ch in t:
        count[ch] -= 1
    for val in count.values():
        if val != 0:
            return False
    return True

print(isAnagram('anagram', 'nagaram')) # returns True
print(isAnagram('anagram', 'nam')) # returns False
print(isAnagram('aaca', 'ssss')) # returns False