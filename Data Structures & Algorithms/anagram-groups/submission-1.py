class Solution:

    def construct_hashmap(self, s):
        hm = {}
        for i in range(len(s)):
            if s[i] not in hm: 
                hm[s[i]]=1
            else: 
                hm[s[i]]+=1

        chars = sorted(hm.keys())

        ret = ""

        for c in chars: 
            ret += c
            ret += str(hm[c])

        return ret

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            a = self.construct_hashmap(s)

            if a in hm:
                hm[a].append(s)
            else: 
                hm[a]= [s]
        
        return [hm[a] for a in hm.keys()]


            