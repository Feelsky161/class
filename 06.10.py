"""count=int(input("введите число:  "))
count = ()
while count > 0:
    print("123"), end=" "
    count-=1
"""
"""a=0
count = int(input(" "))
while a<= count:
    print(a, end=" ")
    a+=1"""
"""n=int(input("введите число: "))
sum = 0
while  n>0:
    sum+=n
    n-=1
print(sum)
"""
"""n=int(input("число: "))
sum=0
a=1
while a<=n:
    sum+=a
    print(f"{a}+", end="")
    a+=1
print(f"\b={sum}")
"""
'''n=int(input("введите число: "))
a=0
while a<=n:
    print(a, end=" ")
    a+=2(тут можно break)
'''
'''n=int(input("введите число: "))
a=0
while True:
    print(a, end=" ")
    a+=1
    if a>n:
        break
'''
'''import random
pcnam=random.randint(1,3)
"""print(pcnam)"""
while True:
    playernam=int(input("1-камень 2-ножницы 3-бумага: "))
    if not (playernam== 1 or playernam==2 or playernam==3):
        break
    print("не тупи...")'''
import random
pcnam=random.randint(1,3)
game_count=0
playerwin=0
pcwin=0

"""print(pcnam)"""
while True:
    game_count+=1
    playernam=int(input("1-камень 2-ножницы 3-бумага: "))
    if playernam in (1,2,3):
        break
    print("не тупи...")

pcstr= "камень"
playerstr= "камень"

print(f"пк: {pcstr} игрок {playerstr}")
if playernam==pcnam:
    print("ничья")
elif playernam==1:
    print("пк победил" if pcnam==3 else "пк проиграл")
elif playernam==2:
    print("пк победил" if pcnam==1 else "пк проиграл")
elif playernam ==3:
    print("пк победил" if pcnam ==2 else "пк проиграл")

    again=input("введите 1 если хотите продолжить: ")
    if again!="1":
        breakpoint()
    print()