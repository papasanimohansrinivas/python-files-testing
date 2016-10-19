from itertools import product
from itertools import combinations
"""input1 = int(raw_input())"""
noOftestcases=int(raw_input())
output=[]
for l1 in range(noOftestcases):
    list_of_strings = []
    input1= int(raw_input())

    for h in xrange(input1):
        list_of_strings.append(raw_input())

    lists_of_subsequences=[]

    def ispalindrome(t):

        i=""
        for so in t[::-1]:
            i=i+so

        if(i==t):
            return True
        else:
            return False
            

        

    def sub_sequences(l):
        answer=[]
        r=len(l)
        while(r!=0):
            for y in  combinations(l,r):
                answer.append("".join(y))
            r=r-1
        #print answer
        return answer

    for j in (list_of_strings):
        ##print sub_sequences(j),
        lists_of_subsequences.append(sub_sequences(j))

        
    count = 0
    
    for k in product(*lists_of_subsequences):
        #print k
        t=""
        for l in k:
            t=t+(l)
        #print t
        if(ispalindrome(t)):
            count=count+1
            
       
            
    output.append(count%((10**9)+7))

    
    
for h in range(noOftestcases):
    print output[h]

        
