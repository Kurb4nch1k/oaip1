def main():
    with open("words.txt", encoding="utf-8") as a:
        word = a.read().split()
        print(min(word), max(word)))


if __name__ == "__main__":
    main()