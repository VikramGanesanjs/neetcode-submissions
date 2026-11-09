class Solution:
    def construct_hashmap(self, s):
        hm = [0 for i in range(26)]
        for i in range(len(s)):
            hm[ord(s[i])-ord('a')]+=1

        return hm

        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            a = self.construct_hashmap(s)

            hm[tuple(a)].append(s)
        
        return [hm[a] for a in hm.keys()]


            