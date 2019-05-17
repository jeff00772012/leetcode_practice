def reverse(x: int) -> int:

     num_str=str(abs(x))
     new_num=int(num_str[::-1])
     if new_num > 2**31-1:
      return 0
     else:
      if x >= 0:
       return new_num
      else: 
       return -new_num


a=reverse(-123)
print(a)