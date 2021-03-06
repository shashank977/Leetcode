# test cases 1:  s = "abc", t = "ahbgdc"
# test cases 2:  s = "axc", t = "ahbgdc"
        
              
# (1)        
def isSubsequence(s, t):
    
    s_pointer =0
    t_pointer =0
        
    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1
    return s_pointer == len(s)
        
        
        
# (2)       
def isSubsequence(s, t):
    s_pointer = 0
    t_pointer = 0
        
    if s == "":
        return True


    while t_pointer < len(t) and s_pointer < len(s):
        if t[t_pointer] == s[s_pointer]:
            s_pointer+=1
            if s_pointer == len(s):
                return True
        t_pointer+=1
            
    return False
    
        
        
#(3)        
def is_subsequence(s, t):
    if s == "":
        return True

    s_pointer=0

    for i in range(len(t)):
        if t[i]==s[s_pointer]:
            s_pointer+=1
        if s_pointer==len(s):
            return  True

    return s_pointer==len(s)        
