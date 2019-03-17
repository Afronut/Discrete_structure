def cardinality(a, b):
    a = set(a)
    b = set(b)
    a_b = a.difference(b)
    b_a = b.difference(a)
    c = a.intersection(b)
    print(a_b)
    print(b_a)
    print(c)


if __name__ == "__main__":
    A = {2, 3, 4, 5, 7, 8, 9, 10}
    B = {1, 5, 6, 7, 8, 9, 10}
    cardinality(A, B)
