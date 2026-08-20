class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {} # this is an empty dictionary 

        for word in strs : 
            key = "".join(sorted(word)) # sorted(word) return list of characters and this line joins the characters into the string
                                        # so now the key is sorted word e.g act
            if key not in group :
                group[key] = []         # here e.g { [act : [] ]}
            
            group[key].append(word)   # here {[act : [act]]}
        
        return list(group.values())



        

        
        