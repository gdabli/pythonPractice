# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict

def findAnagram(words):
    dict = defaultdict(list)
    list_of_anagrams = []
    # create a dictionary of all anagrams
    for word in words:
        dict["".join(sorted(word))].append(word)
    #print(dict)

    # import all values in list and print
    for value in dict.values():
        list_of_anagrams.append(value)

    print(list_of_anagrams)

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    findAnagram(strs)