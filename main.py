from pprint import pprint

def dict_collector(file_work):
    with open(file_work, 'r', encoding='utf-8') as file:
        menu = {}
        for line in file:
            dish_name = line[:-1]
            counter = file.readline().strip()
            grocery_list = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = file.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                grocery_list.append(dish_items)
                cook_book = {dish_name: grocery_list}
                menu.update(cook_book)
            file.readline()

    return(menu)

dict_collector('recipes.txt')

def get_shop_list_by_dishes(dishes, persons=int):

    menu = dict_collector('recipes.txt')
    print('Наше меню выглядит вот так:')
    pprint(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):

                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list.update(items_list)

        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)