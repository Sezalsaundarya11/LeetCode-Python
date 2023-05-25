class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
       

        # using counter

        count1 , count2 = Counter(ransomNote), Counter(magazine)

        if count1 & count2 == count1:
            return True
        return False
         """

        #  using list
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter," ",1)
            else:
                return False
        return True



