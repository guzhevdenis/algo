# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        anagrams[key].append(s)


    return list(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))