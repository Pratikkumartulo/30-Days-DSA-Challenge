'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.'''

class Solution(object):
    def lengthOfLastWord(self, s):
        list1=s.split(" ")
        for i in list1[::-1]:
            if i!='':
                return len(i)
                break
        