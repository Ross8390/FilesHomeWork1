with open('data.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient = f.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
            'ingredient_name': ingredient_name,
            'quantity': quantity,
            'measure': measure
            })
        f.readline()
        cook_book[dish_name] = ingredients
print(cook_book)