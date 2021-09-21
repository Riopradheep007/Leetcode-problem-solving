"""                               
                           ##########################################################################################33
                                                            Find Common Character
                           ############################################################################################

    Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
         check = list(words[0])
         for word in words:
            newCheck = []
            for w in word:
                
                if w in check:
                    newCheck.append(w)
                    check.remove(w)
            check = newCheck
         return check
            
