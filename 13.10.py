"""list1 = [1,2,3,4,5]
print(list1)
for i in range (0,4):
    print(list1[i], end=" ")
for i in list1:
    print(i, end=" ")
"""


"""spis = [1,2,3,4,5,6]
for i in range (5):
    if spis[i]% 2 ==0:
        spis[i]=0
print(spis)"""


'''spis1=[1,2,3,4,5,6]
for i in spis1:
    if i%2==0:
        i=0
print(spis1)'''


"""counter=[4,2,3,4,4,6,2,5,7,3,7,8]
www=0
for i in range(len(counter)):
    for j in range(len(counter)):
        if i==j:
            continue
        if counter[i]==counter[j]:
            www+=1
            break
print(len(counter)-www)"""

#замена переменных местами
'''www=[1,2,3,4,5,6,7,8,9]
for i in range(len(www)//2):
        www[i],www[len(www)-i-1]=www[len(www)-i-1],www[i]
print(www)'''


'''www=[1,2,3,4,5]
sum=0
for i in www:
    sum+=i
print(sum/len(www))'''

'''www=[1,2,3,4,5]
sum=0
for i in range(len(www)):
    sum+=www[i]
print(sum/len(www))'''


'''www1=[1,2,3,4,5,6,7]
www2=[1,2,3,4,5]
for i in www1:
    flag=True
    for j in www2:
        if i==j:
            flag=False
            break
    if flag:
        print(i, end=" ")'''


'''www1 = [1, 2, 3, 4, 5, 6, 7]
www2 = [1, 2, 3, 4, 5]
www3 = set(www1) - set(www2)
www4 = set(www2) - set(www1)
difference = www3.union(www4)
print(list(difference))'''


'''www1=[1,2,3,4,5,6,7]
www2=[1,2,3,4,5]
for i in www1:
    flag=False
    for j in www2:
        if i==j:
            flag=True
            break
    if flag:
        print(i, end=" ")'''


'''www1=[1,2,3,4,5,6,7]
www2=[1,2,3,4,5]
for i in www1:
    if i in www2:
        print(i, end=" ")'''



'''numbers = [1, 2, 3, 4, 2, 2, 5, 2, 6]

n = int(input("Введите число: "))

count = numbers.count(n)

print(f"Число {n} встречается в списке {count} раз")'''


'''numbers = [1, 2, 3, 4, 2, 2, 5, 2, 6]
num= int(input("число"))
counter=0
for i in numbers:
    if num==i:
        counter+=1
print(counter)'''
while True:
    try:
    num =int(input("введите число: "))
    print("ошибка введите число")
    break
except:
    print("введите число")
print(num)