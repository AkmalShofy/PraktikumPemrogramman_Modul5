def maksimal(a,b) :
    if a > b : return a
    else : return b
def minimal(a,b) :
    if a < b : return a
    else : return b
batas = 0
maks = -100000
minim = 100000
bilangan = int(input())
while batas < bilangan : 
    nilai1 = map(int,input().split())
    for nilai in nilai1 :
        maks = maksimal(maks, nilai)
        minim = minimal(minim, nilai)
        batas+=1
print("%d %d" % (maks,minim))