def proc1():

    input('Введите пароль.')
    print('Пароль принят' if input() == input() else 'Пароль не принят')


def proc2():

    n = int(input('Введите номер вашего места в плацкартном вагоне: '))
    print()
    if n > 54:
        print('Некорректно введен номер места')
    elif n > 36:
        print('Ваше место - боковое.')
    elif n % 2:
        print('Ваше место в купе внизу.')
    else:
        print('Ваше место в купе наверху.')


def proc3():

    year = int(input('Введите номер года: '))
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Год високосный')
    else:
        print('Год не високосный')

def proc4():

    a = ('Красный', 'Синий', 'Желтый')
    c1 = input()
    c2 = input()
    if c1 in a and c2 in a:
        if (c1 in ('Красный', 'Синий')) and (c2 in ('Красный', 'Синий')):
            print('фиолетовый')
        if (c1 in ('Желтый', 'Синий')) and (c2 in ('Желтый', 'Синий')):
            print('Зеленый')
        if (c1 in ('Красный', 'Желтый')) and (c2 in ('Красный', 'Желтый')):
            print('Оранжевый')
    else:
        print('Цвет введен неверно')

'''
def proc5():
    n = int(input())
    result = []
    for i in range(n):
        result.append(input())
    word = ' '.join(result)
    print(word)

def proc6():
    words = []
    while (new_word := str(input())) != "stop":
        words.append(new_word)
    print(" ".join(words))

def proc7():
    words = []
    while (new_word := str(input())) !="stop":
        if "ф" in new_word or "Ф" in new_word:
            print('Ого, это редкое слово!')
        else:
            print('Это обычно слово')
        words.append(new_word)
    print(" ".join(words))
proc3()

'''
