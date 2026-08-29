# Valid Anagrams

def isAnagram(s, t):

    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# Using hashmap

from collections import Counter

def isAnagram(s, t):

    return Counter(s) == Counter(t)

# Grouping Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            key = ''.join(sorted(word))

            group.setdefault(key, []).append(word)

        return list(group.values())
