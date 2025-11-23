from television import Television  # import statement needed to gain access to Television class


def main():
    # Television 1
    tv_1 = Television()
    print(tv_1)
    tv_1.power()
    print(tv_1)
    tv_1.power()
    print(tv_1)

if __name__ == '__main__':
    main()
