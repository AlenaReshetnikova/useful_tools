import random


def change_to_str(num):
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'


def work(num):
    phone = []
    for i in number:
        if i.isdigit():
            ya = random.choice(["y", 'n'])
            if ya == 'y':
                i = change_to_str(int(i))
            phone.append(i)
            phone.append(random.choice([" ", ' , ', ' - ']))
    return phone


PHONE = '(737) 262-1095'
number = list(PHONE)
print(''.join(work(number)))
