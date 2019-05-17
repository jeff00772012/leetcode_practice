def isPalindrome(x: int) -> bool:
    if (x < 0) | ((x%10)==0 & x!=0):
     return False
    else:
     num_str=str(x)
     rever=num_str[::-1]
     if rever == num_str:
      return True
     else:
      return False
   
a=isPalindrome(0)
print(a)       