list=['Raymond','Park avenue','Van Heusen','Blackberry','Zodiac']
def droplist(number):
    lyst=[]
    for i in range(0,number):
       lyst.append(list[i])
    return lyst
def takelist(number):
    lyst=[]
    for i in range(number,len(list)):
       lyst.append(list[i]) 
    return lyst
delist=droplist(2)
alist=takelist(3)
print delist
print alist

