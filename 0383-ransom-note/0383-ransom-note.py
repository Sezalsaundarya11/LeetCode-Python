class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # using counter

        count1 , count2 = Counter(ransomNote), Counter(magazine)

        if count1 & count2 == count1:
            return True
        return False

