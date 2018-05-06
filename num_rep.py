def num_rep(s):
    
    temp = ""
        
    for i in range(len(s)):

        temp += str(ord(s[i]))

    return int(temp)


print(num_rep("hi"))
print(num_rep("h")+num_rep("i"))
                
