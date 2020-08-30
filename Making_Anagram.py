def makingAnagrams(s1, s2):
    k=[]
    s1=list(s1)
    s2=list(s2)
    if(len(s1)>len(s2)):
        for char in s1:
            if char in s2:
                k.append(char)
                s2.remove(char) 
        return ((len(s1)-len(k))+len(s2))            
    else:
        for char in s2:
            if char in s1:
                k.append(char)
                s1.remove(char)
        return ((len(s2)-len(k))+len(s1)) 