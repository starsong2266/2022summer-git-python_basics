#開啟、讀取文件檔
article = open('2022summer-git-python_basics/HW1/HW1.txt','r')
content = article.read()
#print(content)
article.close()

#計算句子個數
sentence_list = content.split('.')
del sentence_list[len(sentence_list)-1]#最後一個元素會是''，需刪除
sentence_num = len(sentence_list)

#建立句子長度統計器
def counter(sentence_list, characters = None, trim = False): 
    a=0 
    b=0
    c=0
    d=0
    e=0
    f=0
    num_stc_with_characters = 0
    detector = False
    
    for stc in sentence_list:
        
        if trim:
            for x in characters:
                if x in stc:
                    stc = stc.replace(x,'')
                    detector = True
            if detector:
                num_stc_with_characters += 1
                detector = False
        
        if stc == sentence_list[0]:
            len_stc = len(stc)+1#第一句，補上拆分時去掉的句點
        else:
            len_stc = len(stc)-1#其他句，補上拆分時去掉的句點，然後消除換行符號'\n'佔據的長度

        if len_stc <= 40:
            a+=1
        elif len_stc <= 50:
            b+=1
        elif len_stc <= 60:
            c+=1
        elif len_stc <= 70:
            d+=1
        elif len_stc <= 80:
            e+=1
        else:
            f+=1
        
    if not trim:
        return a, b, c, d, e, f
    return a, b, c, d, e, f, num_stc_with_characters

#計算句子長度
#修除亂碼前
a, b, c, d, e, f = counter(sentence_list)
print(a+b+c+d+e+f == sentence_num)

#修除亂碼後
characters = '!?+-'
g, h, i, j, k, l, num = counter(sentence_list, characters, trim = True)
print(g+h+i+j+k+l == sentence_num)


#將結果輸出成文件檔
HW1 = open('2022summer-git-python_basics/HW1_王亭堅/HW1_王亭堅.txt','w')
HW1.write(f'There are {sentence_num} sentences in HW1.txt. {num} of them include !?+-.\n')
HW1.write('length before trim after trim\n')
HW1.write(f'  <=40 {a:11d}{g:11d}\n')
HW1.write(f'  <=50 {b:11d}{h:11d}\n')
HW1.write(f'  <=60 {c:11d}{i:11d}\n')
HW1.write(f'  <=70 {d:11d}{j:11d}\n')
HW1.write(f'  <=80 {e:11d}{k:11d}\n')
HW1.write(f'   >80 {f:11d}{l:11d}\n')
HW1.close()