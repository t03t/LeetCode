class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # type color name
        # items = [[type,color,name], [type,color, name]] etc
        
        output = 0
        ind = ["type","color","name"].index(ruleKey)
        
        for item in items:
            if item[ind]==ruleValue:
                output+=1
        return output
        