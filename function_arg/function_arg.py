def avg(*items):

    items_list = []

    for item in items:
        if isinstance(item, (int, float)):
            items_list.append(item)

    result = sum(items_list) / len(items)

    return print(f'{result:.2f}')


avg(0.8, 'qwer', 1.2, 500.323424)
