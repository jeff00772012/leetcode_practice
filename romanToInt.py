def romanToInt(s: str) -> int:
    dic_roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    idx=0
    num=[]
    num.append(dic_roman[s[0]])
    for roman in (range(len(s)-1)):
        word_cur=s[roman]
        word_next=s[roman+1]
        if (dic_roman[word_cur]==dic_roman[word_next]):
            idx = idx
            num[idx] = num[idx]+dic_roman[word_next]
        elif (dic_roman[word_cur]>dic_roman[word_next]):
            idx = idx +1
            num.append(dic_roman[word_next])
        else:
            num[idx]=(dic_roman[word_next]-num[idx])
            #idx = idx+1
        print(num)
        print(idx)
    return sum(num)
a=romanToInt('MCMXCIV')
print(a)
