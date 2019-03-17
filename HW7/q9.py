def sequence_slayer(n):
    if n == 1:
        return 1
    series = [1, 2]
    for i in range(2, n+1):
        a_n = (i) ** 2 * series[-1] - series[-2]
        series.append(a_n)
    return series


if __name__ == "__main__":
    print(sequence_slayer(10))
