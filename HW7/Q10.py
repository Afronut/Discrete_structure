def first_D_digit_Lucas(n):
    series = [2, 1]
    while True:
        a_n = series[-1] + series[-2]
        series.append(a_n)
        if len(str(series[-1])) == n:
            return series[-1]


if __name__ == "__main__":
    print(first_D_digit_Lucas(3))
