def climbStairs(n: int) -> int:
    a=1
    b=1
    if n < 2:
        return 1
    else:
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 

print(climbStairs(3))