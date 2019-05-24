def addBinary(a: str, b: str) -> str:
    length=[len(a),len(b)]
    big = length.index(max(length))
    c=[a,b]
    num=[0,0]
    count=1
    for x in range(max(length)):
        
        if (len(a)!=len(b))&(x > min(length)-1):
            num[big]=num[big]+(int(c[big][x])*(2**(len(c[big])-count)))
            count = count+1
 
        else:
            num[0] = num[0]+(int(c[0][x])*(2**(len(a)-count)))
            num[1] = num[1]+(int(c[1][x])*(2**(len(b)-count)))   
            count = count+1
            print(num)
        
    sum_num = bin(sum(num))
    return sum_num[2:]             

print(addBinary("11","1"))
       