#print ('There are XXXX sentences in HW1.txt. XXXX of them include !?+-.length before trim after trim')
# strip string =>delete ?+-
import re
#with open('C:/Users/b0861/Desktop/Python_Project/C4lab/2022summer-git-python_basics/HW1/HW1.txt', 'r') as f:
 #   a = f.read()
a = "Praesent blandit odio sit amet risus eleifend elementum.Nulla cond?+--!??+--!?imentum massa quis ante porta, eget fermentum sapien cursus."

c = "ahiahi"
print(c.strip("i"))
print(c)
#print(a)
for i in a:
    i.strip('?+-!')
    i.strip('\n')
    #print(i)
b = a.strip('?')   
c = b.split('.')

#print(b)
#print(c)
NumOfSen = len(b)
new_lst = [re.sub("[^A-z]", "", s) for s in b]

#print("-------")
#print(new_lst)
print(NumOfSen)


#print(a)
#print('\n')
#print(re.sub(r'[^\w]', '', a))
#print(a)
