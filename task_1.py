with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        indigrients_count = int(f.readline())
        indigrients = []
        for i in range(indigrients_count):
            ind = f.readline().strip()
            name, quantity, measure = ind.split(' | ')
            indigrients.append({'indigrient_name': name, 'quantity': quantity, 'measure': measure})
        f.readline()
        cook_book[dish] = indigrients
print(cook_book)
