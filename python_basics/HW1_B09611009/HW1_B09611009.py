f = open('HW1.txt')

SENTENCE=[]
TrimmedSENTENCE=[]
characters="!?+-"
r=0
r1=0
L_40=0;L_50=0;L_60=0;L_70=0;L_80=0;L_80UP=0
TL_40=0;TL_50=0;TL_60=0;TL_70=0;TL_80=0;TL_80UP=0
for line in f.readlines():    
    SENTENCE.append(line.replace('\n',''))
    #print('Original Line:',SENTENCE[r])

    for x in range (len(characters)):
        line=line.replace(characters[x],'')

    TrimmedSENTENCE.append(line.replace('\n',''))
    #print('Trimmed Line:',TrimmedSENTENCE[r],'\n')
    r+=1 
    #print('ROW:',r,'\n')
f.close

for i in range(r):
    sign = False
    L = len(SENTENCE[i])
    TL = len(TrimmedSENTENCE[i])
    if(L<=40): L_40+=1
    elif(L<=50): L_50+=1
    elif(L<=60): L_60+=1
    elif(L<=70): L_70+=1
    elif(L<=80): L_80+=1
    else: L_80UP+=1

    if(TL<=40): TL_40+=1
    elif(TL<=50): TL_50+=1
    elif(TL<=60): TL_60+=1
    elif(TL<=70): TL_70+=1
    elif(TL<=80): TL_80+=1
    else: TL_80UP+=1

    for j in range(L):
        if (SENTENCE[i][j]=='!'or SENTENCE[i][j]=='?' or SENTENCE[i][j]=='-' or SENTENCE[i][j]=='+'):
            sign = True
    if(sign == True):
        r1 += 1

print('There are',r,'sentences in HW1.txt.',r1,'of them include !?+-.')
print('length before trim after trim')
print('{0:>6}'.format('<=40'),'{0:>11}'.format(L_40),'{0:>10}'.format(TL_40))
print('{0:>6}'.format('<=50'),'{0:>11}'.format(L_50),'{0:>10}'.format(TL_50))
print('{0:>6}'.format('<=60'),'{0:>11}'.format(L_60),'{0:>10}'.format(TL_60))
print('{0:>6}'.format('<=70'),'{0:>11}'.format(L_70),'{0:>10}'.format(TL_70))
print('{0:>6}'.format('<=80'),'{0:>11}'.format(L_80),'{0:>10}'.format(TL_80))
print('{0:>6}'.format('>80'),'{0:>11}'.format(L_80UP),'{0:>10}'.format(TL_80UP))
"""
c=0
for y in range (r):
    if(len(SENTENCE[y])<=40):
        c=c+1
        print(c,len(SENTENCE[y]),SENTENCE[y])
"""
path='HW1_B09611009.txt'
Output=open(path,'w')
print('There are',r,'sentences in HW1.txt.',r1,'of them include !?+-.', file=Output)
print('length before trim after trim', file=Output)
print('{0:>6}'.format('<=40'),'{0:>11}'.format(L_40),'{0:>10}'.format(TL_40), file=Output)
print('{0:>6}'.format('<=50'),'{0:>11}'.format(L_50),'{0:>10}'.format(TL_50), file=Output)
print('{0:>6}'.format('<=60'),'{0:>11}'.format(L_60),'{0:>10}'.format(TL_60), file=Output)
print('{0:>6}'.format('<=70'),'{0:>11}'.format(L_70),'{0:>10}'.format(TL_70), file=Output)
print('{0:>6}'.format('<=80'),'{0:>11}'.format(L_80),'{0:>10}'.format(TL_80), file=Output)
print('{0:>6}'.format('>80'),'{0:>11}'.format(L_80UP),'{0:>10}'.format(TL_80UP), file=Output)
Output.close()
