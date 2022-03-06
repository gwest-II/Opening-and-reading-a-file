import json

cook_book = {}
def cook_book_dict():
    #cook_book = {}
    keys = ['ingridient_name', 'quantity', 'measure', ]
    with open('recipes.txt', encoding='utf-8') as file:
        lines = []
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)
            continue
        lines = iter(lines)

        for name in lines:
            cook_book[name] = []
            num = next(lines)
            for _ in range(int(num)):
                stuff_line = next(lines)
                ingrid = stuff_line.split('|')
                z = zip(keys, ingrid)
                stuff_dict = {k: v for (k, v) in z}
                cook_book[name].append(stuff_dict)
                continue
            continue

    print(json.dumps(cook_book,indent=4, ensure_ascii=False))
cook_book_dict()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:


