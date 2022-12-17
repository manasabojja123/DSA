#Python program for checking two arrays are equal or not
#True or False
l1=[1,2,3,1,4,1,1]
l2=[1,2,3,1,4,1,1]
n1=[]
n2=[]
n3=[]
n4=[]
for i in l1:
    if(i not in n1):
        n1.append(i)
for i in l2:
    if(i not in n2):
        n2.append(i)
n1.sort()
n2.sort()
if(n1==n2):
    for i in n1:
        n3.append(l1.count(i))
        n4.append(l2.count(i))
    
    n3.sort()
    n4.sort()
    if(n3==n4):
        print(True)

    else:
        print(False)
else:
    print(False)
    


    
        
            
