import math
def prim(a,b):
    diferenta=abs(a-b)
    if diferenta<2 :
       return False
    for i in range(2,int(diferenta/2)):
       if diferenta%i==0: return False
    return True
# ----------------------
lst=[2,4,6,8,10]

def cerinta(lst):
    """
lst ..


"""
maxim=1
poz=1
maxi=1
for i in range (len(lst)-1):
    if prim(lst[i],lst[i+1])==True:
        maxi=maxi+1
        if maxi>maxim:
            maxim=maxi
            poz=i+1
    else:
        maxi=1
start=poz-maxim+1
poz=poz+1
print(maxim)
print(start)
print(poz)
for i in range(start,poz):
    print(lst[i])
#-------------------------

cerinta(lst)


