def print_even_odd_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    print("Even lines:")
    for i in range(0, len(lines), 2):
        print(lines[i].strip())

    print("Odd lines:")
    for i in range(1, len(lines), 2):
        print(lines[i].strip())

# Вызов функции
print_even_odd_lines('lines.txt')
