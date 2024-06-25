def main():
    with open("lines.txt", encoding="utf-8") as a:
        b = 0
        for line in a:
            b += len(line)
        c = b * 8
        d = b
        e = b / 1000
        f = b / 106
        g = b / 109
        h = b / 10 ** 12
    print(c, "бит")
    print(d, "байт")
    print(e, "мегабайт")
    print(f, "мегабайт")
    print(g, "гигабайт")
    print(h, "терабайт")


if __name__ == "__main__":
    main()