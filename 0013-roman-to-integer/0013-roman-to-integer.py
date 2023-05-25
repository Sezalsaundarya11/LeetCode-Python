class Solution(object):
    def romanToInt(self, s):
        map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        i=0
       
        while i<len(s):
            if i <len(s)-1 and  map[s[i]] < map[s[i+1]]:
                sum+=(map[s[i+1]]-map[s[i]])
                i+=2
            else:
                sum+=map[s[i]]
                i+=1 
        return sum


        