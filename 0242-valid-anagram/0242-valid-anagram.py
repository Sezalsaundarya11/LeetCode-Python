class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False

        list1 = list(s)

        for i in s:
            if i in t:
                t=t.replace(i,'',1)
            else:
                return False
        return True