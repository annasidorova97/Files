cook_book = {}


def cook_book_reader(file_name:str, mode:str, encoding:str):
    with open(file_name, mode, encoding=encoding) as file:
        for recipe in file.read().split('\n\n'):
            food_name, ingredients_quantity, *ingredients = recipe.split('\n')
            cook_book[food_name] = []
            for ingredient in ingredients:
                ingredient_str = ingredient.split(' | ')
                ingredient_dict = {}
                ingredient_dict['ingredient_name'] = ingredient_str[0]
                ingredient_dict['quantity'] = ingredient_str[1]
                ingredient_dict['measure'] = ingredient_str[2]
                cook_book[food_name].append(ingredient_dict)
    print(f'cook_book =\n{cook_book}')


def get_shop_list_by_dishes(dishes:list, person_count:int):
    shop_list = {}
    dish_list = []
    for dish in dishes:
        if dish not in dish_list:
            dish_list.append(dish)
            for ingredient in cook_book[dish]:
                quantity_of_ingredient = {}
                quantity_of_ingredient['measure'] = ingredient['measure']
                sum_quantity = int(ingredient['quantity']) * person_count * dishes.count(dish)
                quantity_of_ingredient['quantity'] = sum_quantity
                shop_list[ingredient['ingredient_name']] = quantity_of_ingredient
    print(shop_list)


cook_book_reader('recipes.txt', 'r', 'utf-8')
print('')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 2)
