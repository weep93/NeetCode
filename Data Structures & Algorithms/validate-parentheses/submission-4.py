class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        marks = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        for line in s:
   
            if line in marks: #marking the opening 
                stack.append(line)
            if line in marks.values():
                #checking if its empty
                if stack:
                    recent_opening = stack.pop()
                    expected = marks[recent_opening]

                    if line != expected:
                        return False
                else:
                    return False
            

        return not stack
            


        
