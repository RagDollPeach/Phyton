cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]


def print_tax():
    salary = int(input("Введите зарабатную плату: "))
    enter_home_tax = int(input("Введите, какой процент(%) уходит на ипотеку: "))
    enter_used_many = int(input("Введите, какой процент(%) уходит на жизнь: "))

    home_tax = int(salary * enter_home_tax / 100)
    used_many = int(salary * enter_used_many / 100)
    saved_many = int(salary - (home_tax + used_many))

    print("На ипотеку было потрачено: ", home_tax, "рублей")
    print("На жизнь было потрачено: ", used_many, "рублей")
    print("Было накопено: ", saved_many, "рублей")


def print_figure():
    height = int(input("Введите высоту фигуры: "))
    length = int(input("Введите длинну фигуры: "))

    if height == length:
        print("Площадь квадрата -", height * length)
        print("Длнна периметра квадрата -", (height + length) * 2)
    else:
        print("Площадь прямоугольника -", height * length)
        print("Длнна периметра прямоугольника-", (height + length) * 2)


def ideal_mate():
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)

    pairs = zip(sorted_boys, sorted_girls)
    print('Идеальные пары:')

    for pair in pairs:
        print(f'{pair[0]} и {pair[1]}')


def chef_book():
    persons = input('Persons number - ')
    print()
    for dish in cook_book:
        print(f'{dish[0].capitalize()}: ')
        for ingredients in dish[1]:
            print(f'{ingredients[0]}, {ingredients[1] * int(persons)}{ingredients[2]}')
        print()


def sort_list(geo_logs):
    my_list = [{}]
    for my_dict in geo_logs:
        for key, val in my_dict.items():
            if val[1] == 'Россия':
                my_list.append(my_dict)
    for my_dict in my_list:
        for key, val in my_dict.items():
            print(f'{key} - {val[0]}, {val[1]}')
    print()


def my_set(ids):
    my_list = []
    for key, val in ids.items():
        for my_id in val:
            my_list.append(my_id)
    print(set(my_list))


def count_words(queries):
    one_word = 0
    two_words = 0
    three_words = 0
    more_then_3 = 0

    for words in queries:
        match len(words.split()):
            case 1:
                one_word += 1
            case 2:
                two_words += 1
            case 3:
                three_words += 1
            case  _:
                more_then_3 += 1

    summ = one_word + two_words + three_words + more_then_3

    print(f'Запрос из одного слова: {round((one_word / summ) * 100, 1)}% \n'
          f'Запрос из двух слов: {round((two_words / summ) * 100, 1)}% \n'
          f'Запрос из трех слов: {round((three_words / summ) * 100, 1)}% \n'
          f'Запрос из более чем трех слов: {round((more_then_3 / summ) * 100, 1)}%')


def simple_sort(stats):
    max_digit = 0
    name = ''
    for key, val in stats.items():
        if val > max_digit:
            max_digit = int(val)
            name = str(key)
    print(name)
