def read_prices_file(filename):
    total_cost = 0.0

    try:
        with open(filename, 'r') as file:
            for line in file:
                columns = line.strip().split('\t')
                if len(columns) == 3:
                    quantity = float(columns[1])
                    price = float(columns[2])
                    total_cost += quantity * price
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

    return total_cost

filename = "prices.txt"
total_cost = read_prices_file(filename)
print(f"Общая стоимость заказа: {total_cost:.2f}")
