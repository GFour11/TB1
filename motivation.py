import random
def foo_2():
    file= open('2.txt', 'r', -1, 'utf-8')
    data = file.read()
    data = data.split("\n")
    j=random.choice(data)
    return j
