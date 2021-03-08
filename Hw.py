import itertools


def main():
    print("This is demonstrating infinite iterators cycle and repeat")
    t = [52, 54, 58, 63, 70, 75, 65]  # average temp in tampa last week
    count = 0
    for n in itertools.cycle(t):
        if count > 10:
            break
        else:
            print(n, end=" ")
            count += 1

    print(list(itertools.repeat(t, 3)))


if __name__ == "__main__":
    main()
