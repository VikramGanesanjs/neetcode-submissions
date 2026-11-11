class Solution:

    def encode(self, strs: List[str]) -> str:
        num_str = ""
        ret_str = ""
        for s in strs:
            ret_str += s
            num_str += str(len(s)) + " "
        
        fin = ret_str + "é" + num_str
        return fin

    def decode(self, s: str) -> List[str]:
        split = s.split("é")
        ret_str, num_str = split[0], split[1]
        num_list = num_str[:-1].split(" ")
        ret = []
        if num_list[0] == '':
            return []
        
        for num in num_list:
            ret.append(ret_str[:int(num)])
            ret_str = ret_str[int(num):]

        return ret