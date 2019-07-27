def convert(r): 
    if(len(r)==0): 
        return
    r1='' 
    r1+=r[0].upper() 
    for i in range(1,len(r)- 1): 
        if(r[i] ==' '): 
            r1+=r[i+1].upper() 
            i+=1
        elif(r[i - 1]!=' '): 
            r1+=r[i]  
    print(r1)      
def main(): 
    r=input()
    convert(r)   
if __name__=="__main__": 
    main()
