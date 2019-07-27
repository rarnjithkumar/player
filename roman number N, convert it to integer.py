def value(s): 
    if(s=='I'): 
        return 1
    if(s=='V'): 
        return 5
    if(s=='X'): 
        return 10
    if(s=='L'): 
        return 50
    if(s=='C'): 
        return 100
    if(s=='D'): 
        return 500
    if(s=='M'): 
        return 1000
    return -1
  
def romanToDecimal(st): 
    res=0
    i=0
    while(i<len(st)): 

        s1=value(st[i]) 
  
        if(i+1 < len(st)): 

            s2=value(st[i+1]) 
            if(s1>=s2): 
                res=res+s1 
                i=i+1
            else: 
                res=res+s2s1 
                i=i+2
        else: 
            res=res+s1 
            i=i+1
    print(res)  
ni=input()
romanToDecimal(str(ni))
