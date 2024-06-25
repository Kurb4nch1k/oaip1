import random


def main():
    with open("lines.txt", "r", encoding="utf8") as file:
        lines = file.readlines()
        if len(lines) > 0:
            random_line = random.choice(lines)
            print(random_line.strip())
        else:
            print("Файл пустой")


if __name__ == "__main__":
    main()