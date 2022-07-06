a=[]                #before trim how many words in a sentence

b=[]                #after trim words in a sentence

ansbeftrim=[0]*6    #計數結果
ansafttrim=[0]*6    #計數結果







charnum=0

char="!?+-"
with open ('/home/b07204037/2022summer-git-python_basics/HW1/HW1.txt','r')as f:    #讀檔案存入list
    lines = f.readlines()

howlong=len(lines)                     #算幾行


for n in range(539):                   #算有多少含有標點符號
 for x in range(len(char)):           
       if char[x] in lines[n]:
        charnum=charnum+1
        break
    



for i in range(539):
    a.append(len(lines[i])-1)                  #計算每行多長放入一個list且扣掉換行
    
a[538]=a[538]+1                                #最後一行不換行


for i in range(539):#計數
    if (a[i]<=40):
        ansbeftrim[0]=ansbeftrim[0]+1
    if (a[i]<=50 and a[i]>40):
        ansbeftrim[1]=ansbeftrim[1]+1
    if (a[i]>50 and a[i]<=60):
        ansbeftrim[2]=ansbeftrim[2]+1
    if (a[i]>60 and a[i]<=70):
        ansbeftrim[3]=ansbeftrim[3]+1
    if (a[i]>70 and a[i]<=80):
        ansbeftrim[4]=ansbeftrim[4]+1
    if (a[i]>80):
        ansbeftrim[5]=ansbeftrim[5]+1
        
    


with open ('/home/b07204037/2022summer-git-python_basics/HW1/HW1.txt','r')as f:
    trimlines = f.readlines()


for n in range(539):
 for x in range(len(char)):            #計算亂碼長度，由第一個扣到最後一個，重複至文末
        trimlines[n]=trimlines[n].replace(char[x],"")


for i in range(539):                   #計算每行多長放入一個list且扣掉換行
    b.append(len(trimlines[i])-1) 
    

b[538]=b[538]+1                        #最後一行不換行

for i in range(539):                   #計數器
    if (b[i]<=40):
        ansafttrim[0]=ansafttrim[0]+1
    if (b[i]<=50 and b[i]>40):
        ansafttrim[1]=ansafttrim[1]+1
    if (b[i]>50 and b[i]<=60):
        ansafttrim[2]=ansafttrim[2]+1
    if (b[i]>60 and b[i]<=70):
        ansafttrim[3]=ansafttrim[3]+1
    if (b[i]>70 and b[i]<=80):
        ansafttrim[4]=ansafttrim[4]+1
    if (b[i]>80):
        ansafttrim[5]=ansafttrim[5]+1
        


print(howlong)    
print(charnum)
print("before trim",ansbeftrim,"\n")        
print("after trim",ansafttrim)





charn=str(charnum)
long=str(howlong)


with open('/home/b07204037/2022summer-git-python_basics/HW1_b07204037/HW1_b07204037.txt' , 'w') as f: #寫入一個檔案叫做HW1b07204037
  
    f.write("There are "+long+" sentences in HW1.txt. "+charn +" of them include !?+-."+"\n") 
    f.write("length before trim after trim"+"\n")
    for i in range(4,9):
        n=str(i)
        f.write(('{0:>6}'.format('<='+n+"0"))+('{0:>12}'.format(ansbeftrim[i-4]))+('{0:>11}'.format(ansafttrim[i-4]))+"\n")

    f.write(('{0:>6}'.format('>80'))+('{0:>12}'.format(ansbeftrim[5]))+('{0:>11}'.format(ansafttrim[5]))+"\n")

    
    