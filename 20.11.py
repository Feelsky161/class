"""with open("123.txt", "r", encoding='utf-8') as file:
        print(len(file.readlines()))
        file.seek(0)
        print(file)"""

"""with open("123.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    print(len(lines))
    for i in lines:
        print(i)
    """
"""import re
file = ("123.txt")
with open("123.txt", "r", encoding='utf-8') as file:
    text = file.read()
    listik = re.split("['\s\n']",text)
    counter=0
    for i in listik:
        if i =="ggg":
            counter +=1
        print(counter)"""

"""with open("123.txt", "r", encoding='utf-8') as file:
    print(file.read())
with open("123copy.txt", "w") as file:
    file.write("ggg")"""
"""def file_copy(path):
    with open(path, encoding="utf-8") as file:
        text = file.read()
    index =path.rfind(".")
    new_path = path[:index]+'copy.txt'
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

file_copy("src/st.txt")"""
vocabular = ("уй","ой")
def cenzer(path):
    with open(path, "r+", encoding='utf-8') as file:
    text = file.read()
    result_list = re.split("['\s\n']",text)
    for i in result_list:
        if i in vocabular:
            result_list.remuve(i)

cenzer(("123.txt"))




