items = {}
while True:
    try:
        item = input().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        sorted_items = dict(sorted(items.items(), key=lambda item: item[0]))
        for item in sorted_items:
            print(f"{sorted_items[item]} {item}")
        break