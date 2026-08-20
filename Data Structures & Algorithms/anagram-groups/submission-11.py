

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for values in strs : 
            key = "".join(sorted(values))

            if key not in dic : 
                dic[key]= []

            dic[key].append(values)

        return list(dic.values())
