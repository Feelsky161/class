"""count=int(input("введите число:  "))
count = ()
while count > 0:
    print("123.txt"), end=" "
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
'''import random

game_count=0
player_win=0
pc_win=0

while True:
    game_count+=1
    pc_number=random.randint(1,3)
    while True:
        player_number=int(input("1-камень 2-ножницы 3-бумага: "))
        if player_number in (1,2,3):
            break
        print("не тупи...")
    pc_str="камень"
    player_str = "камень"
    if pc_number==2:
        pc_str="ножницы"
    elif pc_number==3:
        pc_str="бумага"

    if player_number==2:
        player_str="ножницы"
    elif player_number==3:
        player_str="бумага"

    print(f"пк: {pc_str} игрок: {player_str}")
    if player_number==pc_number:
        print("ничья")
    elif player_number==1:
        if pc_number == 3:
            print("пк победил")
            pc_win+=1
        else:
            print("пк проиграл")
            player_win+=1
    elif player_number==2:
        if pc_number == 1:
            print("пк победил")
            pc_win+=1
        else:
            print("пк проиграл")
            player_win+=1
    elif player_number==3:
        if pc_number == 2:
            print("пк победил")
            pc_win+=1
        else:
            print("пк проиграл")
            player_win+=1

    print(f"побед пк: {pc_win} побед игрока: {player_win} ничьи:{game_count-pc_win-player_win}")
    again = input("введите 1 если хотите сыграть еще раз: ")
    if again!="1":
        break
    print()

print(f"сыграно игр {game_count}")
'''