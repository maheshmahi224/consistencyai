def count(fname):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    wc,vc,bsc,lcc,ucc=0,0,0,0,0
    with open(fname,'r') as f:
        for line in f:
            words=line.split()
            wc+=len(words)
    with open(fname,'r') as f:
        for word in f:
            if word in vowels:
                vc+=1
            if word == '':
                bsc+=1
            if word>='a' and word<='z':
                lcc+=1
            if word>='A' and word<='Z':
                ucc+=1
    print(wc)                                
    print(vc)                                
    print(bsc)                                
    print(lcc)                                
    print(ucc)
count('C:/Users/DELL/Desktop/python files/mahesh.txt')                                    