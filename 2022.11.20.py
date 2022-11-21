list1=[1,5,4,8,6]
list2=[1,2,5,8,6,3,4,7]
set1=set(list1)
set2=set(list2)
set3=set1&set2
print(set3)

      
str1=input('请输入一段字母：')
str1.lower()
tuple1=tuple(i for i in str1)
ket=[tuple1.count(i) for i in tuple1]
dict1=dict(zip(tuple1,ket))
print(dict1)

print('下面将随机打印十个8位密码：')
import random
su=0
while su<10:
  secter=random.choices('abcdefghijklmnopqrstuvwxvz0123456789',k=8)
  su+=1
  secter2=''.join(secter)
  print(secter2)

  
str2=input('请输入您的电话号码：')
df=str2.startswith('1')
aq=str2.isdigit()
if len(str2)==11:
  print(True)
  if (df and aq==1):
    print('您输入的是一个电话号码。')
else:
  print('您输入的不是一个电话号码。')
        
 
