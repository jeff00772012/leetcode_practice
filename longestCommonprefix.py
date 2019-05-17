def longestCommonPrefix(strs: [str]) -> str:
 if len(strs) > 1:
    shortest_word=len(min(strs,key=len))
    count=0
    check=True

    for idx in range(shortest_word):
       cha1=strs[0][idx:(idx+1)] 
       
       for word in range(len(strs)-1):
           if strs[word+1][idx:(idx+1)]!=cha1:
               check=False
               break
       if check==True:
           count = count +1  
       
              
    if count > 0:
       return strs[0][0:count]
    else:
       return ""
 elif len(strs) == 1:
       return strs[0]
 else:
       return ""

a=longestCommonPrefix(["abcd","abgg"])
print(a)

