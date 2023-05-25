class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        maxWel=0
        sum=0;

        for acc in accounts:
            for i in acc:
                sum+=i
            maxWel=max(maxWel,sum)
            sum=0

        return maxWel
     