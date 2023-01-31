def get_shop_list_by_dishes(dishes, person_count):
    with open('recipes.txt', 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            indigrients_count = int(file.readline())
            indigrients = {}
            for i in range(indigrients_count):
                ind = file.readline().strip()
                indig, quantity, measure = ind.split(' | ')
                indigrients[indig] = {'measure': measure, 'quantity': int(quantity) * person_count}
            file.readline()
            cook_book[dish] = indigrients
        final_list = {}
        for k in dishes:
            final_list |= cook_book[k]
        print(final_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)